from __future__ import annotations
import builtins as _builtins
import dataclasses as _dataclasses
import typing as _typing

identifier = str
int = int
string = str | bytes
constant = str | bytes | int | float | complex | bool | tuple | frozenset | None | type(...)


class AST:
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = []
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = []


@_dataclasses.dataclass
class mod(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Script(mod):
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    annotations: _builtins.list[string] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["body", "annotations"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Expression(mod):
    body: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["body"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class stmt(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class FunctionDef(stmt):
    name: identifier = _dataclasses.field(default=None)
    args: _builtins.list[param] = _dataclasses.field(default_factory=_builtins.list)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    method: int | None = _dataclasses.field(default=None)
    export: int | None = _dataclasses.field(default=None)
    annotations: _builtins.list[string] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "name",
        "args",
        "body",
        "method",
        "export",
        "annotations",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class TypeDef(stmt):
    name: identifier = _dataclasses.field(default=None)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    export: int | None = _dataclasses.field(default=None)
    annotations: _builtins.list[string] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["name", "body", "export", "annotations"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Assign(stmt):
    target: expr = _dataclasses.field(default=None)
    value: expr | None = _dataclasses.field(default=None)
    type: expr | None = _dataclasses.field(default=None)
    mode: decl_mode | None = _dataclasses.field(default=None)
    annotations: _builtins.list[string] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["target", "value", "type", "mode", "annotations"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class ReAssign(stmt):
    target: expr = _dataclasses.field(default=None)
    value: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["target", "value"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class AugAssign(stmt):
    target: expr = _dataclasses.field(default=None)
    op: operator = _dataclasses.field(default=None)
    value: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["target", "op", "value"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Import(stmt):
    namespace: identifier = _dataclasses.field(default=None)
    name: identifier = _dataclasses.field(default=None)
    version: int = _dataclasses.field(default=None)
    alias: identifier | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["namespace", "name", "version", "alias"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Expr(stmt):
    value: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Break(stmt):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Continue(stmt):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class expr(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class BoolOp(expr):
    op: bool_op = _dataclasses.field(default=None)
    values: _builtins.list[expr] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["op", "values"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class BinOp(expr):
    left: expr = _dataclasses.field(default=None)
    op: operator = _dataclasses.field(default=None)
    right: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["left", "op", "right"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class UnaryOp(expr):
    op: unary_op = _dataclasses.field(default=None)
    operand: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["op", "operand"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Conditional(expr):
    test: expr = _dataclasses.field(default=None)
    body: expr = _dataclasses.field(default=None)
    orelse: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["test", "body", "orelse"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Compare(expr):
    left: expr = _dataclasses.field(default=None)
    ops: _builtins.list[compare_op] = _dataclasses.field(default_factory=_builtins.list)
    comparators: _builtins.list[expr] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["left", "ops", "comparators"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Call(expr):
    func: expr = _dataclasses.field(default=None)
    args: _builtins.list[arg] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["func", "args"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Constant(expr):
    value: constant = _dataclasses.field(default=None)
    kind: string | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "kind"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Attribute(expr):
    value: expr = _dataclasses.field(default=None)
    attr: identifier = _dataclasses.field(default=None)
    ctx: expr_context = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "attr", "ctx"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Subscript(expr):
    value: expr = _dataclasses.field(default=None)
    slice: expr | None = _dataclasses.field(default=None)
    ctx: expr_context = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "slice", "ctx"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Name(expr):
    id: identifier = _dataclasses.field(default=None)
    ctx: expr_context = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["id", "ctx"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Tuple(expr):
    elts: _builtins.list[expr] = _dataclasses.field(default_factory=_builtins.list)
    ctx: expr_context = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["elts", "ctx"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class ForTo(expr):
    target: expr = _dataclasses.field(default=None)
    start: expr = _dataclasses.field(default=None)
    end: expr = _dataclasses.field(default=None)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    step: expr | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["target", "start", "end", "body", "step"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class ForIn(expr):
    target: expr = _dataclasses.field(default=None)
    iter: expr = _dataclasses.field(default=None)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["target", "iter", "body"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class While(expr):
    test: expr = _dataclasses.field(default=None)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["test", "body"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class If(expr):
    test: expr = _dataclasses.field(default=None)
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    orelse: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["test", "body", "orelse"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Switch(expr):
    cases: _builtins.list[case] = _dataclasses.field(default_factory=_builtins.list)
    subject: expr | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["cases", "subject"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Qualify(expr):
    qualifier: type_qual = _dataclasses.field(default=None)
    value: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["qualifier", "value"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Specialize(expr):
    value: expr = _dataclasses.field(default=None)
    args: expr = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "args"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class decl_mode(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Var(decl_mode):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class VarIp(decl_mode):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class type_qual(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Const(type_qual):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Input(type_qual):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Simple(type_qual):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Series(type_qual):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class expr_context(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Load(expr_context):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Store(expr_context):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class bool_op(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class And(bool_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Or(bool_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class operator(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Add(operator):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Sub(operator):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Mult(operator):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Div(operator):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Mod(operator):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class unary_op(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Not(unary_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class UAdd(unary_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class USub(unary_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class compare_op(AST):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Eq(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class NotEq(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Lt(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class LtE(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Gt(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class GtE(compare_op):
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class param(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Param(param):
    name: identifier = _dataclasses.field(default=None)
    default: expr | None = _dataclasses.field(default=None)
    type: expr | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["name", "default", "type"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class arg(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Arg(arg):
    value: expr = _dataclasses.field(default=None)
    name: identifier | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "name"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class case(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Case(case):
    body: _builtins.list[stmt] = _dataclasses.field(default_factory=_builtins.list)
    pattern: expr | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["body", "pattern"]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class cmnt(AST):
    lineno: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    col_offset: int = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_lineno: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    end_col_offset: int | None = _dataclasses.field(default=None, repr=False, compare=False, kw_only=True)
    _attributes: _typing.ClassVar[_builtins.list[_builtins.str]] = [
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]
    __hash__ = _builtins.object.__hash__


@_dataclasses.dataclass
class Comment(cmnt):
    value: string = _dataclasses.field(default=None)
    kind: string | None = _dataclasses.field(default=None)
    _fields: _typing.ClassVar[_builtins.list[_builtins.str]] = ["value", "kind"]
    __hash__ = _builtins.object.__hash__


__all__ = [
    "identifier",
    "int",
    "string",
    "constant",
    "AST",
    "mod",
    "Script",
    "Expression",
    "stmt",
    "FunctionDef",
    "TypeDef",
    "Assign",
    "ReAssign",
    "AugAssign",
    "Import",
    "Expr",
    "Break",
    "Continue",
    "expr",
    "BoolOp",
    "BinOp",
    "UnaryOp",
    "Conditional",
    "Compare",
    "Call",
    "Constant",
    "Attribute",
    "Subscript",
    "Name",
    "Tuple",
    "ForTo",
    "ForIn",
    "While",
    "If",
    "Switch",
    "Qualify",
    "Specialize",
    "decl_mode",
    "Var",
    "VarIp",
    "type_qual",
    "Const",
    "Input",
    "Simple",
    "Series",
    "expr_context",
    "Load",
    "Store",
    "bool_op",
    "And",
    "Or",
    "operator",
    "Add",
    "Sub",
    "Mult",
    "Div",
    "Mod",
    "unary_op",
    "Not",
    "UAdd",
    "USub",
    "compare_op",
    "Eq",
    "NotEq",
    "Lt",
    "LtE",
    "Gt",
    "GtE",
    "param",
    "Param",
    "arg",
    "Arg",
    "case",
    "Case",
    "cmnt",
    "Comment",
]
