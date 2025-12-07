# SPDX-FileCopyrightText: 2025 Yunseong Hwang
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import ast as pyast
import contextlib
import typing

from collections import ChainMap

import click

import pynescript.ast as pyneast

from pynescript.ast import NodeVisitor


class PinescriptToPynecoreScriptTransformer(NodeVisitor):
    def __init__(self):
        self._inputs = []
        self._variables = ChainMap()

    def enter_block(self):
        self._variables = self._variables.new_child()

    def exit_block(self):
        self._variables = self._variables.parents

    @contextlib.contextmanager
    def local_block(self):
        self.enter_block()
        try:
            yield
        finally:
            self.exit_block()

    def visit_Script(self, node: pyneast.Script) -> pyast.Module:
        body = []

        for stmt in node.body:
            result = self.visit(stmt)
            if result is not None:
                if isinstance(result, list):
                    body.extend(result)
                else:
                    body.append(result)

        decl_stmt = body[0]

        if not isinstance(decl_stmt, pyast.Expr):
            msg = "no declaration statement, first statement is not an expression"
            raise ValueError(msg)

        if not isinstance(decl_stmt.value, pyast.Call):
            msg = "no declaration statement, first statement is not a function call"
            raise ValueError(msg)

        if not isinstance(decl_stmt.value.func, pyast.Name):
            msg = "no declaration statement, function is not simple name"
            raise ValueError(msg)

        if decl_stmt.value.func.id not in {"indicator", "strategy", "library"}:
            msg = f"no declaration statement, function name is not in [indicator, strategy, library] but {decl_stmt.value.func.id}"
            raise ValueError(msg)

        return pyast.Module(
            body=body,
            type_ignores=[],
        )

    def visit_Expression(self, node: pyneast.Expression) -> pyast.Expression:
        body = self.visit(node.body)
        return pyast.Expression(
            body=body,
        )

    def visit_FunctionDef(self, node: pyneast.FunctionDef) -> pyast.FunctionDef:
        with self.local_block():
            name = node.name
            args_and_defaults = [self.visit(arg) for arg in node.args]
            args_and_defaults = typing.cast(list[tuple[pyast.arg, pyast.expr | None]], args_and_defaults)
            args = [arg for arg, default in args_and_defaults]
            defaults = [default for arg, default in args_and_defaults if default is not None]
            args = pyast.arguments(
                posonlyargs=[],
                args=args,
                kwonlyargs=[],
                kw_defaults=[],
                defaults=defaults,
            )
            body = [self.visit(stmt) for stmt in node.body]
            decorator_list = []
            func_def = pyast.FunctionDef(
                name=name,
                args=args,
                body=body,
                decorator_list=decorator_list,
            )
            return func_def

    def visit_TypeDef(self, node: pyneast.TypeDef):
        msg = f"unsupported node {node}"
        raise ValueError(msg)

    def visit_Assign(self, node: pyneast.Assign) -> pyast.Assign | pyast.AnnAssign:
        var_type = node.type
        var_mode = node.mode

        target = self.visit(node.target)
        value = self.visit(node.value)

        return pyast.Assign(
            targets=[target],
            value=value,
        )

    def visit_ReAssign(self, node: pyneast.ReAssign) -> pyast.Assign | pyast.AnnAssign:
        target = self.visit(node.target)
        value = self.visit(node.value)

        return pyast.Assign(
            targets=[target],
            value=value,
        )

    def visit_AugAssign(self, node: pyneast.AugAssign) -> pyast.AugAssign:
        target = self.visit(node.target)
        op = self.visit(node.op)
        value = self.visit(node.value)
        return pyast.AugAssign(
            target=target,
            op=op,
            value=value,
        )

    def visit_Import(self, node: pyneast.Import) -> pyast.Import:
        name = f"lib.{node.namespace}.{node.name}.v{node.version}"
        asname = node.alias
        return pyast.Import(
            names=[
                pyast.alias(
                    name=name,
                    asname=asname,
                )
            ]
        )

    def visit_Expr(self, node: pyneast.Expr) -> pyast.Expr:
        value = self.visit(node.value)
        if isinstance(value, pyast.stmt):
            return value
        return pyast.Expr(value=value)

    def visit_Break(self, node: pyneast.Break) -> pyast.Break:
        return pyast.Break()

    def visit_Continue(self, node: pyneast.Continue) -> pyast.Continue:
        return pyast.Continue()

    def visit_BoolOp(self, node: pyneast.BoolOp) -> pyast.BoolOp:
        op = self.visit(node.op)
        values = [self.visit(value) for value in node.values]
        return pyast.BoolOp(
            op=op,
            values=values,
        )

    def visit_BinOp(self, node: pyneast.BinOp) -> pyast.BinOp:
        left = self.visit(node.left)
        op = self.visit(node.op)
        right = self.visit(node.right)
        return pyast.BinOp(
            left=left,
            op=op,
            right=right,
        )

    def visit_UnaryOp(self, node: pyneast.UnaryOp) -> pyast.UnaryOp:
        op = self.visit(node.op)
        operand = self.visit(node.operand)
        return pyast.UnaryOp(
            op=op,
            operand=operand,
        )

    def visit_Conditional(self, node: pyneast.Conditional) -> pyast.IfExp:
        test = self.visit(node.test)
        body = self.visit(node.body)
        orelse = self.visit(node.orelse)
        return pyast.IfExp(
            test=test,
            body=body,
            orelse=orelse,
        )

    def visit_Compare(self, node: pyneast.Compare) -> pyast.Compare:
        left = self.visit(node.left)
        ops = [self.visit(op) for op in node.ops]
        comparators = [self.visit(comp) for comp in node.comparators]
        return pyast.Compare(
            left=left,
            ops=ops,
            comparators=comparators,
        )

    def visit_Call(self, node: pyneast.Call) -> pyast.Call:
        func = self.visit(node.func)
        args_and_keywords = [self.visit(arg) for arg in node.args]
        args = [arg for arg in args_and_keywords if isinstance(arg, pyast.expr)]
        keywords = [keyword for keyword in args_and_keywords if isinstance(keyword, pyast.keyword)]
        call = pyast.Call(
            func=func,
            args=args,
            keywords=keywords,
        )

        return call

    def visit_Constant(self, node: pyneast.Constant) -> pyast.Constant:
        value = node.value
        kind = None
        constant = pyast.Constant(
            value=value,
            kind=kind,
        )
        return constant

    def visit_Attribute(self, node: pyneast.Attribute) -> pyast.Attribute | pyast.Name:
        value = self.visit(node.value)
        attr = node.attr
        ctx = self.visit(node.ctx)
        return pyast.Attribute(
            value=value,
            attr=attr,
            ctx=ctx,
        )

    def visit_Subscript(self, node: pyneast.Subscript) -> pyast.Subscript:
        if not node.slice:
            value = pyast.Name(
                id="array",
                ctx=pyast.Load(),
            )
            slice = self.visit(node.value)
            ctx = self.visit(node.ctx)
            return pyast.Subscript(
                value=value,
                slice=slice,
                ctx=ctx,
            )
        value = self.visit(node.value)
        slice = self.visit(node.slice)
        ctx = self.visit(node.ctx)
        return pyast.Subscript(
            value=value,
            slice=slice,
            ctx=ctx,
        )

    def visit_Name(self, node: pyneast.Name) -> pyast.Name:
        id = node.id
        ctx = self.visit(node.ctx)
        return pyast.Name(
            id=id,
            ctx=ctx,
        )

    def visit_Tuple(self, node: pyneast.Tuple) -> pyast.Tuple:
        elts = [self.visit(elt) for elt in node.elts]
        ctx = self.visit(node.ctx)
        return pyast.Tuple(
            elts=elts,
            ctx=ctx,
        )

    def visit_ForTo(self, node: pyneast.ForTo) -> pyast.For:
        with self.local_block():
            target = self.visit(node.target)
            body = [self.visit(stmt) for stmt in node.body]
            start = self.visit(node.start)
            end = self.visit(node.end)
            step = self.visit(node.step) if node.step else None
            args = [start, end]
            if step:
                args.append(step)
            iter = pyast.Call(
                func=pyast.Name(id="range", ctx=pyast.Load()),
                args=args,
                keywords=[],
            )
            orelse = []
            return pyast.For(
                target=target,
                iter=iter,
                body=body,
                orelse=orelse,
            )

    def visit_ForIn(self, node: pyneast.ForIn) -> pyast.For:
        with self.local_block():
            target = self.visit(node.target)
            body = [self.visit(stmt) for stmt in node.body]
            iter = self.visit(node.iter)
            orelse = []
            return pyast.For(
                target=target,
                iter=iter,
                body=body,
                orelse=orelse,
            )

    def visit_While(self, node: pyneast.While) -> pyast.While:
        with self.local_block():
            test = self.visit(node.test)
            body = [self.visit(stmt) for stmt in node.body]
            orelse = []
            return pyast.While(
                test=test,
                body=body,
                orelse=orelse,
            )

    def visit_If(self, node: pyneast.If) -> pyast.If:
        with self.local_block():
            test = self.visit(node.test)
            body = [self.visit(stmt) for stmt in node.body]
            orelse = [self.visit(stmt) for stmt in node.orelse]
            return pyast.If(
                test=test,
                body=body,
                orelse=orelse,
            )

    def visit_Switch(self, node: pyneast.Switch) -> pyast.Match | pyast.If:
        with self.local_block():
            if node.subject:
                subject = self.visit(node.subject)
                cases = [self.visit(case) for case in node.cases]
                return pyast.Match(
                    subject=subject,
                    cases=cases,
                )
            case = node.cases[-1]
            case = typing.cast(pyneast.Case, case)
            if case.pattern:
                test = self.visit(case.pattern)
                body = self.visit(case.body)
                if_chain = pyast.If(
                    test=test,
                    body=body,
                    orelse=[],
                )
            else:
                if_chain = self.visit(case.body)
            for case in reversed(node.cases[:-1]):
                case = typing.cast(pyneast.Case, case)
                test = self.visit(case.pattern)
                body = self.visit(case.body)
                if_chain = pyast.If(
                    test=test,
                    body=body,
                    orelse=[if_chain],
                )
            if not isinstance(if_chain, pyast.If):
                if_chain = pyast.If(
                    test=pyast.Constant(
                        value=True,
                        kind=None,
                    ),
                    body=if_chain,
                    orelse=[],
                )
            return if_chain

    def visit_Qualify(self, node: pyneast.Qualify) -> pyast.Subscript:
        return pyast.Subscript(
            value=self.visit(node.qualifier),
            slice=self.visit(node.value),
            ctx=pyast.Load(),
        )

    def visit_Specialize(self, node: pyneast.Specialize) -> pyast.expr:
        value = self.visit(node.value)
        slice = self.visit(node.args)
        return pyast.Subscript(
            value=value,
            slice=slice,
            ctx=pyast.Load(),
        )

    def visit_Var(self, node: pyneast.Var):
        return pyast.Name("var", pyast.Load())

    def visit_VarIp(self, node: pyneast.VarIp):
        return pyast.Name("varip", pyast.Load())

    def visit_Const(self, node: pyneast.Const):
        return pyast.Name("const", pyast.Load())

    def visit_Input(self, node: pyneast.Input):
        return pyast.Name("input", pyast.Load())

    def visit_Simple(self, node: pyneast.Simple):
        return pyast.Name("simple", pyast.Load())

    def visit_Series(self, node: pyneast.Series):
        return pyast.Name("series", pyast.Load())

    def visit_Load(self, node: pyneast.Load) -> pyast.Load:
        return pyast.Load()

    def visit_Store(self, node: pyneast.Store) -> pyast.Store:
        return pyast.Store()

    def visit_And(self, node: pyneast.And) -> pyast.And:
        return pyast.And()

    def visit_Or(self, node: pyneast.Or) -> pyast.Or:
        return pyast.Or()

    def visit_Add(self, node: pyneast.Add) -> pyast.Add:
        return pyast.Add()

    def visit_Sub(self, node: pyneast.Sub) -> pyast.Sub:
        return pyast.Sub()

    def visit_Mult(self, node: pyneast.Mult) -> pyast.Mult:
        return pyast.Mult()

    def visit_Div(self, node: pyneast.Div) -> pyast.Div:
        return pyast.Div()

    def visit_Mod(self, node: pyneast.Mod) -> pyast.Mod:
        return pyast.Mod()

    def visit_Not(self, node: pyneast.Not) -> pyast.Not:
        return pyast.Not()

    def visit_UAdd(self, node: pyneast.UAdd) -> pyast.UAdd:
        return pyast.UAdd()

    def visit_USub(self, node: pyneast.USub) -> pyast.USub:
        return pyast.USub()

    def visit_Eq(self, node: pyneast.Eq) -> pyast.Eq:
        return pyast.Eq()

    def visit_NotEq(self, node: pyneast.NotEq) -> pyast.NotEq:
        return pyast.NotEq()

    def visit_Lt(self, node: pyneast.Lt) -> pyast.Lt:
        return pyast.Lt()

    def visit_LtE(self, node: pyneast.LtE) -> pyast.LtE:
        return pyast.LtE()

    def visit_Gt(self, node: pyneast.Gt) -> pyast.Gt:
        return pyast.Gt()

    def visit_GtE(self, node: pyneast.GtE) -> pyast.GtE:
        return pyast.GtE()

    def visit_Param(self, node: pyneast.Param) -> tuple[pyast.arg, pyast.expr | None]:
        arg = node.name
        annotation = self.visit(node.type) if node.type else None
        arg = pyast.arg(arg=arg, annotation=annotation)
        default = self.visit(node.default) if node.default else None
        return arg, default

    def visit_Arg(self, node: pyneast.Arg) -> pyast.expr | pyast.keyword:
        arg = node.name
        value = self.visit(node.value)
        return (
            pyast.keyword(
                arg=arg,
                value=value,
            )
            if arg
            else value
        )

    def visit_Case(self, node: pyneast.Case) -> pyast.match_case:
        if not node.pattern:
            pattern = pyast.MatchAs()
        elif isinstance(node.pattern, pyneast.Constant):
            value = node.pattern.value
            if isinstance(value, bool):
                pattern = pyast.MatchSingleton(value=value)
            else:
                value = pyast.Constant(value=value)
                pattern = pyast.MatchValue(value=value)
        else:
            value = self.visit(node.pattern)
            pattern = pyast.MatchValue(value=value)
        body = [self.visit(stmt) for stmt in node.body]
        return pyast.match_case(
            pattern=pattern,
            body=body,
        )

    def visit_Comment(self, node: pyneast.Comment):
        msg = f"unsupported node {node}"
        raise ValueError(msg)


def compile(content: str) -> str:
    transformer = PinescriptToPynecoreScriptTransformer()
    pynescript_ast = pyneast.parse(content)
    pynecore_ast = transformer.visit_Script(pynescript_ast)
    pynecore_ast = pyast.fix_missing_locations(pynecore_ast)
    code = pyast.unparse(pynecore_ast)
    return code


@click.command
@click.argument("filename", type=click.Path())
def main(filename):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    click.echo(compile(content))


if __name__ == "__main__":
    main()
