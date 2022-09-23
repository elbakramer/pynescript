from inspect import Parameter
from inspect import signature
from typing import Callable
from typing import Generic
from typing import Optional
from typing import TypeVar
from typing import Union

from pyparsing import Empty
from pyparsing import Forward
from pyparsing import Group
from pyparsing import IndentedBlock
from pyparsing import OneOrMore
from pyparsing import ParseElementEnhance
from pyparsing import ParserElement
from pyparsing import ParseResults
from pyparsing import TokenConverter
from pyparsing import col
from pyparsing import lineno

from pynescript.ast.parser.utils import calc_width
from pynescript.ast.parser.utils import calc_width_col
from pynescript.ast.types import AST


T = TypeVar("T")


class ResultNameableForward(Forward):
    def __init__(self, other: Optional[Union[ParserElement, str]] = None):
        super().__init__(other)
        self._copies_should_forward_to = []

    def __lshift__(self, other):
        super().__lshift__(other)
        for copy in self._copies_should_forward_to:
            copy.__lshift__(other)
        return self

    def _setResultsName(self, name, list_all_matches=False):
        # pylint: disable=protected-access
        copy = ParseElementEnhance._setResultsName(self, name, list_all_matches)
        self._copies_should_forward_to.append(copy)
        return copy


class IndentPeerDetect(Empty):
    def __init__(self, ref_col: int):
        super().__init__()

        def condition(s, l, t):
            # pylint: disable=unused-argument
            cur_col = calc_width_col(l, s)
            return cur_col == ref_col

        message = f"expected indent at column {ref_col}"

        self.add_condition(condition, message=message)

        self.errmsg = message
        self.callDuringTry = True


class IndentedBlockWithTabs(IndentedBlock):
    def __init__(
        self,
        expr: ParserElement,
        recursive: bool = False,
        grouped: bool = True,
        tab_width: int = 4,
    ):
        super().__init__(
            expr,
            recursive=recursive,
            grouped=grouped,
        )
        self._tab_width = tab_width

    def parseImpl(self, instring, loc, doActions=True):
        # advance parse position to non-whitespace by using an Empty()
        # this should be the column to be used for all subsequent indented lines
        anchor_loc = Empty().preParse(instring, loc)

        # see if self.expr matches at the current location - if not it will raise an exception
        # and no further work is necessary
        self.expr.try_parse(instring, anchor_loc, doActions)

        indent_col = col(anchor_loc, instring)
        indent_num_chars = indent_col - 1
        indent_chars = instring[(anchor_loc - indent_num_chars) : anchor_loc]
        indent_width = calc_width(indent_chars, tab_width=self._tab_width)
        indent_width_col = indent_width + 1

        peer_detect_expr = IndentPeerDetect(indent_width_col)

        inner_expr = Empty() + peer_detect_expr + self.expr
        inner_expr.set_name(
            f"inner {hex(id(inner_expr))[-4:].upper()}@{indent_width_col}"
        )

        block = OneOrMore(inner_expr)

        if self._grouped:
            block = Group(block)

        return block.parseImpl(instring, anchor_loc, doActions)


class ConvertToFactoryOutputAction(Generic[T], Callable[[str, int, ParseResults], T]):
    def __init__(self, factory: Callable[..., T]):
        self._factory = factory
        self._factory_signature = signature(self._factory)

        self._args_num = 0
        self._kwargs_names = []

        self._has_var_positional = any(
            param.kind == Parameter.VAR_POSITIONAL
            for name, param in self._factory_signature.parameters.items()
        )
        self._has_var_keyword = any(
            param.kind == Parameter.VAR_KEYWORD
            for name, param in self._factory_signature.parameters.items()
        )

        if not self._has_var_positional:
            self._args_num = len(
                [
                    param
                    for name, param in self._factory_signature.parameters.items()
                    if param.kind
                    in [Parameter.POSITIONAL_ONLY, Parameter.POSITIONAL_OR_KEYWORD]
                ]
            )

        if not self._has_var_keyword:
            self._kwargs_names = [
                param.name
                for name, param in self._factory_signature.parameters.items()
                if param.kind
                in [Parameter.POSITIONAL_OR_KEYWORD, Parameter.KEYWORD_ONLY]
            ]

        self._factory_required_parameters = [
            param
            for name, param in self._factory_signature.parameters.items()
            if param.default is Parameter.empty
        ]

    def __call__(self, instring: str, loc: int, tokenlist: ParseResults) -> T:
        # pylint: disable=arguments-differ

        args = tokenlist.as_list()
        kwargs = tokenlist.as_dict()

        bound_arguments = self._factory_signature.bind_partial()

        if kwargs:
            if not self._has_var_keyword:
                kwargs = {
                    name: value
                    for name, value in kwargs.items()
                    if name in self._kwargs_names
                }

            bound_arguments_kwargs = self._factory_signature.bind_partial(**kwargs)

            for name, value in bound_arguments_kwargs.arguments.items():
                bound_arguments.arguments[name] = value

            bound_arguments.apply_defaults()

            any_missing_argument = any(
                param.name not in bound_arguments.arguments
                for param in self._factory_required_parameters
            )

            if not any_missing_argument:
                args = []

        if args:
            if not self._has_var_positional:
                args = args[: self._args_num]

            bound_arguments_args = self._factory_signature.bind_partial(*args)

            for name, value in bound_arguments_args.arguments.items():
                bound_arguments.arguments[name] = value

        result = self._factory(*bound_arguments.args, **bound_arguments.kwargs)

        return result


class ConverterUsingFactory(TokenConverter, Generic[T]):
    def __init__(self, expr: ParserElement, factory: Callable[..., T]):
        super().__init__(expr)

        self._action = ConvertToFactoryOutputAction(factory)

    def postParse(self, instring, loc, tokenlist) -> T:
        return self._action(instring, loc, tokenlist)


class TrackLocation(ParseElementEnhance):
    def __init__(
        self,
        expr: Union[ParserElement, str],
        savelist: bool = False,
        key: str = "loc",
    ):
        super().__init__(expr, savelist)

        self._key = key

    def parseImpl(self, instring, loc, doActions=True):
        # pylint: disable=protected-access
        pre_loc = loc
        loc, tokens = self.expr._parse(instring, loc, doActions, callPreParse=False)
        post_loc = loc
        pre_lineno = lineno(pre_loc, instring)
        pre_col_offset = col(pre_loc, instring)
        post_lineno = lineno(post_loc, instring)
        post_col_offset = col(post_loc, instring)
        tokens[self._key] = {
            "loc": pre_loc,
            "lineno": pre_lineno,
            "col_offset": pre_col_offset,
            "end_loc": post_loc,
            "end_lineno": post_lineno,
            "end_col_offset": post_col_offset,
        }
        return loc, tokens


class ConverterUsingFactoryToNode(TrackLocation, ConverterUsingFactory[AST]):
    def postParse(self, instring, loc, tokenlist) -> AST:
        node = self._action(instring, loc, tokenlist)
        node.set_attributes(**tokenlist[self._key])
        return node


def ConvertToNode(factory: Callable[..., AST]):
    def Inner(expr: ParserElement):
        return ConverterUsingFactoryToNode(expr, factory)

    return Inner
