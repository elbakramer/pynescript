from __future__ import annotations

from abc import ABC
from typing import Union


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
    def __init__(self, x: Union[PythonBoolType, BoolType]):
        if isinstance(x, BoolType):
            self.x = bool(x)
        else:
            raise TypeError()

    def __bool__(self):
        return self.x

    def __repr__(self):
        return repr(self.x)

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
    def __init__(self, x: Union[PythonStringType, ColorType]):
        if isinstance(x, ColorType):
            self.x = x.x
        elif isinstance(x, PythonStringType):
            self.x = x
        else:
            raise TypeError()

    def __repr__(self):
        type_name = self.__class__.__name__
        type_value = self.x
        return f"{type_name}({type_value})"


class StringType(Type, PythonStringType):
    pass


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
