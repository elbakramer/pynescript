from pyparsing import Char
from pyparsing import Combine
from pyparsing import Literal
from pyparsing import OneOrMore
from pyparsing import Opt
from pyparsing import ZeroOrMore
from pyparsing import srange


D = Char(srange("[0-9]"))
L = Char(srange("[a-zA-Z_]"))
H = Char(srange("[a-fA-F0-9]"))
E = Combine(Char(srange("[Ee]")) + Opt(Char(srange("[+-]"))) + OneOrMore(D))
FS = Literal("f") | Literal("F") | Literal("l") | Literal("L")
IS = Combine(ZeroOrMore(Literal("u") | Literal("U") | Literal("l") | Literal("L")))
