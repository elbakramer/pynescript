from __future__ import annotations

import json

from abc import ABC


PythonIntType = int
PythonFloatType = float
PythonBoolType = bool
PythonStringType = str


class Type(ABC):
    pass


class IntType(Type, PythonIntType):
    pass


class FloatType(Type, PythonFloatType):
    pass


class BoolType(Type):
    def __init__(self, x: PythonBoolType | BoolType | None = None):
        if isinstance(x, BoolType):
            self.x = bool(x)
        else:
            raise TypeError()

    def __bool__(self):
        return self.x

    def __python_repr__(self):
        return repr(self.x)

    def __pinescript_repr__(self):
        return repr(self.x).lower()

    def __repr__(self):
        return self.__python_repr__()

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BoolType:
            if C is PythonBoolType:
                return True
            if any("__bool__" in B.__dict__ for B in C.__mro__):
                return True
            if any("__nonzero__" in B.__dict__ for B in C.__mro__):
                return True
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


class ColorType(Type):
    def __init__(self, x: PythonStringType | ColorType):
        if isinstance(x, ColorType):
            self.x = x.x
        elif isinstance(x, PythonStringType):
            self.x = x
        else:
            raise TypeError()

    def __python_repr__(self):
        type_name = self.__class__.__name__
        type_value = self.x
        return f"{type_name}({type_value})"

    def __pinescript_repr__(self):
        return self.x

    def __repr__(self):
        return self.__python_repr__()


class StringType(Type, PythonStringType):
    def __python_repr__(self):
        return str.__repr__(self)

    def __pinescript_repr__(self):
        return json.dumps(self, ensure_ascii=False)

    def __repr__(self):
        return self.__python_repr__()


class PlotType(Type):
    pass


class HLineType(Type):
    pass


class LineType(Type):
    pass


class LinefillType(Type):
    pass


class LabelType(Type):
    pass


class BoxType(Type):
    pass


class TableType(Type):
    pass


class ArrayType(Type):
    pass


class MatrixType(Type):
    pass


class VoidType(Type):
    pass


class TupleType(Type):
    pass


class NaType(Type):
    pass
