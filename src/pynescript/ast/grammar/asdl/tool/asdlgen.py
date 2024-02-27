# Copyright 2024 Yunseong Hwang
#
# Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import ast
import functools
import itertools

from argparse import ArgumentParser
from pathlib import Path

import pyasdl


class PythonGenerator(pyasdl.ASDLVisitor):
    # ruff: noqa: N802

    def __init__(self, *, defaults: str = "all"):
        self._defaults = defaults
        self._base = ast.Name("AST", ast.Load())
        self._dataclasses = ast.Name("_dataclasses", ast.Load())
        self._dataclass = ast.Attribute(self._dataclasses, "dataclass", ast.Load())
        self._field = ast.Attribute(self._dataclasses, "field", ast.Load())
        self._typing = ast.Name("_typing", ast.Load())
        self._classvar = ast.Attribute(self._typing, "ClassVar", ast.Load())
        self._builtins = ast.Name("_builtins", ast.Load())
        self._object = ast.Attribute(self._builtins, "object", ast.Load())
        self._hash = ast.Attribute(self._object, "__hash__", ast.Load())
        self._assign_hash = ast.Assign([ast.Name("__hash__", ast.Store())], self._hash)
        self._fields = ast.Name("_fields", ast.Store())
        self._attributes = ast.Name("_attributes", ast.Store())
        self._list = ast.Attribute(self._builtins, "list", ast.Load())
        self._str = ast.Attribute(self._builtins, "str", ast.Load())
        self._classvar_list_str = ast.Subscript(
            self._classvar,
            ast.Subscript(
                self._list,
                self._str,
                ast.Load(),
            ),
            ast.Load(),
        )
        self._attribute_keywords = [
            ast.keyword("repr", ast.Constant(value=False)),
            ast.keyword("compare", ast.Constant(value=False)),
            ast.keyword("kw_only", ast.Constant(value=True)),
        ]

    def _generate_internals(self) -> list[ast.ImportFrom | ast.Import]:
        """
        from __future__ import annotations

        import builtins as _builtins
        import dataclasses as _dataclasses
        import typing as _typing
        """
        return [
            ast.ImportFrom("__future__", [ast.alias("annotations")]),
            ast.Import([ast.alias("builtins", self._builtins.id)]),
            ast.Import([ast.alias("dataclasses", self._dataclasses.id)]),
            ast.Import([ast.alias("typing", self._typing.id)]),
        ]

    def _generate_builtin_types(self) -> list[ast.Assign]:
        """
        identifier = str
        int = int
        string = str | bytes
        constant = str | bytes | int | float | complex | bool | tuple | frozenset | type(None) | type(Ellipsis)
        """
        return [
            ast.Assign([ast.Name("identifier", ast.Store())], ast.Name("str", ast.Load())),
            ast.Assign([ast.Name("int", ast.Store())], ast.Name("int", ast.Load())),
            ast.Assign(
                [ast.Name("string", ast.Store())],
                ast.BinOp(ast.Name("str", ast.Load()), ast.BitOr(), ast.Name("bytes", ast.Load())),
            ),
            ast.Assign(
                [ast.Name("constant", ast.Store())],
                functools.reduce(
                    lambda left, right: ast.BinOp(left, ast.BitOr(), right),
                    [
                        ast.Name("str", ast.Load()),
                        ast.Name("bytes", ast.Load()),
                        ast.Name("int", ast.Load()),
                        ast.Name("float", ast.Load()),
                        ast.Name("complex", ast.Load()),
                        ast.Name("bool", ast.Load()),
                        ast.Name("tuple", ast.Load()),
                        ast.Name("frozenset", ast.Load()),
                        ast.Constant(None),
                        ast.Call(ast.Name("type", ast.Load()), [ast.Constant(Ellipsis)], []),
                    ],
                ),
            ),
        ]

    def _generate_base(self) -> ast.ClassDef:
        """
        class AST:
            _fields: ClassVar[list[str]] = []
            _attributes: ClassVar[list[str]] = []
        """
        return ast.ClassDef(
            name=self._base.id,
            body=[
                ast.AnnAssign(self._fields, self._classvar_list_str, ast.List([], ast.Load()), simple=1),
                ast.AnnAssign(self._attributes, self._classvar_list_str, ast.List([], ast.Load()), simple=1),
            ],
            bases=[],
            keywords=[],
            decorator_list=[],
        )

    def _generate_exports(self, names: list[str]) -> ast.Assign:
        """
        ___all___ = [...]
        """
        exports = ast.Assign(
            [ast.Name("__all__", ast.Store())],
            ast.List(
                [ast.Constant(name) for name in names],
                ast.Load(),
            ),
        )
        return exports

    def _fix_attributes(self, attributes: list[ast.AnnAssign]):
        for annassign in attributes:
            if annassign.value is None:
                annassign.value = ast.Call(self._field, [], [])
            annassign.value.keywords.extend(self._attribute_keywords)
        return attributes

    def _assign_attributes(self, attributes: list[ast.AnnAssign]):
        target = self._attributes
        annotation = self._classvar_list_str
        default = ast.List([ast.Constant(attr.target.id) for attr in attributes], ast.Load())
        assign = ast.AnnAssign(target, annotation, default, simple=1)
        return assign

    def _assign_fields(self, fields: list[ast.AnnAssign]):
        target = self._fields
        annotation = self._classvar_list_str
        default = ast.List([ast.Constant(field.target.id) for field in fields], ast.Load())
        assign = ast.AnnAssign(target, annotation, default, simple=1)
        return assign

    def visit_Module(self, node: pyasdl.Module) -> ast.Module:
        internals = self._generate_internals()
        builtins = self._generate_builtin_types()
        base = self._generate_base()
        definitions = list(itertools.chain.from_iterable(self.visit_all(node.body)))
        names = [t.id for b in builtins for t in b.targets] + [self._base.id] + [d.name for d in definitions]
        exports = self._generate_exports(names)
        body = internals + builtins + [base] + definitions + [exports]
        module = ast.Module(body, type_ignores=[])
        return module

    def visit_Type(self, node: pyasdl.Type) -> list[ast.ClassDef]:
        attributes = self.visit_all(node.value.attributes)
        self._fix_attributes(attributes)
        definitions = self.visit(
            node.value,
            name=node.name,
            attributes=attributes,
        )
        if not isinstance(definitions, list):
            definitions = [definitions]
        return definitions

    def visit_Sum(self, node: pyasdl.Sum, name: str, attributes: list[ast.AnnAssign]) -> list[ast.ClassDef]:
        body = []
        if attributes:
            body.extend(attributes)
            body.append(self._assign_attributes(attributes))
        body.append(self._assign_hash)
        cls = ast.ClassDef(
            name=name,
            body=body,
            bases=[self._base],
            keywords=[],
            decorator_list=[self._dataclass],
        )
        definitions = []
        definitions.append(cls)
        definitions.extend(self.visit_all(node.types, base=name))
        return definitions

    def visit_Constructor(self, node: pyasdl.Constructor, base: str) -> ast.ClassDef:
        fields = self.visit_all(node.fields)
        name = node.name
        body = []
        base = ast.Name(base, ast.Load())
        if fields:
            body.extend(fields)
            body.append(self._assign_fields(fields))
        body.append(self._assign_hash)
        cls = ast.ClassDef(
            name=name,
            body=body,
            bases=[base],
            keywords=[],
            decorator_list=[self._dataclass],
        )
        return cls

    def visit_Product(self, node: pyasdl.Product, name: str, attributes: list[ast.AnnAssign]) -> ast.ClassDef:
        fields = self.visit_all(node.fields)
        body = fields + attributes
        if fields:
            body.append(self._assign_fields(fields))
        if attributes:
            body.append(self._assign_attributes(attributes))
        body.append(self._assign_hash)
        cls = ast.ClassDef(
            name=name,
            body=body,
            bases=[self._base],
            keywords=[],
            decorator_list=[self._dataclass],
        )
        return cls

    def visit_Field(self, node: pyasdl.Field) -> ast.AnnAssign:
        target = ast.Name(node.name, ast.Store())
        annotation = ast.Name(node.kind, ast.Load())
        default = None
        if self._defaults == "all":
            default = ast.Call(self._field, [], [ast.keyword("default", ast.Constant(None))])
        if node.qualifier is not None:
            if node.qualifier is pyasdl.FieldQualifier.SEQUENCE:
                annotation = ast.Subscript(self._list, annotation, ast.Load())
                default = ast.Call(self._field, [], [ast.keyword("default_factory", self._list)])
            elif node.qualifier is pyasdl.FieldQualifier.OPTIONAL:
                annotation = ast.BinOp(annotation, ast.BitOr(), ast.Constant(None))
                default = ast.Call(self._field, [], [ast.keyword("default", ast.Constant(None))])
            else:
                msg = f"Unexpected field qualifier: {node.qualifier}"
                raise ValueError(msg)
        if self._defaults == "none":
            default = None
        return ast.AnnAssign(target, annotation, default, simple=1)

    def generate(self, tree: pyasdl.Module) -> ast.Module:
        return self.visit_Module(tree)


def main():
    parser = ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("-o", "--out", default=1)
    options = parser.parse_args()

    with open(options.file, encoding="utf-8") as stream:
        tree = pyasdl.parse(stream.read())

    generator = PythonGenerator()
    stub = generator.generate(tree)

    with open(options.out, "w", encoding="utf-8") as stream:
        stream.write(ast.unparse(ast.fix_missing_locations(stub)))


if __name__ == "__main__":
    main()
