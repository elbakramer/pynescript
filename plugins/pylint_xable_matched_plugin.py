from __future__ import annotations

import re

from pathlib import PurePath
from typing import TYPE_CHECKING

from pylint import exceptions
from pylint.checkers import BaseChecker


if TYPE_CHECKING:
    from tokenize import TokenInfo

    from pylint.lint import PyLinter


class XableMatchedPluginChecker(BaseChecker):

    name = "xable-matched"

    msgs = {
        "C3111": (
            "Matched filepath pattern for disabling rules",
            "matched-disable-paths",
            "Used when pylint found file that should disable some rules",
        ),
        "C3112": (
            "Matched filepath pattern for enabling rules",
            "matched-enable-paths",
            "Used when pylint found file that should enable some rules",
        ),
        "C3113": (
            "Matched filename pattern for disabling rules",
            "matched-disable-patterns",
            "Used when pylint found file that should disable some rules",
        ),
        "C3114": (
            "Matched filename pattern for enabling rules",
            "matched-enable-patterns",
            "Used when pylint found file that should enable some rules",
        ),
    }

    options = (
        (
            "disable-paths",
            {
                "type": "string",
                "metavar": "<pattern>:<msg ids>[ <pattern>:<msg ids>...]",
                "help": "Disable the message, report, category or checker "
                "for files or directories matching the glob or regex patterns "
                "with the given id(s). You can either give multiple identifiers "
                "separated by comma (,) or put this option multiple times "
                "(only on the command line, not in the configuration file "
                "where it should appear only once). "
                'You can also use "--disable-paths=<pattern>:all" to disable everything first '
                "and then re-enable specific checks. For example, if you want "
                "to run only the similarities checker, you can use "
                '"--disable-paths=<pattern>:all --enable-paths=<pattern>:similarities". '
                "If you want to run only the classes checker, but have no "
                "Warning level messages displayed, use "
                '"--disable-paths=<pattern>:all --enable-paths=<pattern>:classes --disable-paths=<pattern>:W".',
            },
        ),
        (
            "enable-paths",
            {
                "type": "string",
                "metavar": "<pattern>:<msg ids>[ <pattern>:<msg ids>...]",
                "help": "Enable the message, report, category or checker "
                "for files or directories matching the glob or regex patterns with the "
                "given id(s). You can either give multiple identifier "
                "separated by comma (,) or put this option multiple time "
                "(only on the command line, not in the configuration file "
                "where it should appear only once). "
                'See also the "--disable-paths" option for examples.',
            },
        ),
        (
            "disable-patterns",
            {
                "type": "string",
                "metavar": "<pattern>:<msg ids>[ <pattern>:<msg ids>...]",
                "help": "Disable the message, report, category or checker "
                "for files or directories matching the glob or regex patterns "
                "with the given id(s). You can either give multiple identifiers "
                "separated by comma (,) or put this option multiple times "
                "(only on the command line, not in the configuration file "
                "where it should appear only once). "
                'You can also use "--disable-patterns=<pattern>:all" to disable everything first '
                "and then re-enable specific checks. For example, if you want "
                "to run only the similarities checker, you can use "
                '"--disable-patterns=<pattern>:all --enable-patterns=<pattern>:similarities". '
                "If you want to run only the classes checker, but have no "
                "Warning level messages displayed, use "
                '"--disable-patterns=<pattern>:all --enable-patterns=<pattern>:classes --disable-patterns=<pattern>:W".',
            },
        ),
        (
            "enable-patterns",
            {
                "type": "string",
                "metavar": "<pattern>:<msg ids>[ <pattern>:<msg ids>...]",
                "help": "Enable the message, report, category or checker "
                "for files or directories matching the glob or regex patterns with the "
                "given id(s). You can either give multiple identifier "
                "separated by comma (,) or put this option multiple time "
                "(only on the command line, not in the configuration file "
                "where it should appear only once). "
                'See also the "--disable-patterns" option for examples.',
            },
        ),
    )

    @classmethod
    def match_glob(
        cls,
        pattern: str,
        filepath: str,
        is_basename: bool = False,
    ) -> bool:
        if is_basename:
            filepath = PurePath(filepath).name
        path = PurePath(filepath)
        matched = path.match(pattern)
        while not matched and path.parent != path:
            path = path.parent
            matched = path.match(pattern)
        return matched

    @classmethod
    def match_regex(
        cls,
        pattern: str,
        filepath: str,
        is_basename: bool = False,
    ) -> bool:
        if is_basename:
            filepath = PurePath(filepath).name
        return re.match(pattern, filepath) is not None

    @classmethod
    def match_path(cls, pattern: str, filepath: str) -> bool:
        return cls.match_glob(pattern, filepath) or cls.match_regex(pattern, filepath)

    @classmethod
    def match_pattern(cls, pattern: str, filepath: str) -> bool:
        return cls.match_glob(pattern, filepath, is_basename=True) or cls.match_regex(
            pattern,
            filepath,
            is_basename=True,
        )

    @classmethod
    def parse_argument_value(cls, string: str):
        if string:
            string = string.strip()
            while string:
                pattern, string = string.split(":", 1)
                tokens = re.split(r"\s+", string, 1)
                if len(tokens) > 1:
                    msgids, string = tokens
                else:
                    msgids, string = tokens[0], ""
                msgids = [msgid.strip() for msgid in msgids.split(",") if msgid.strip()]
                yield pattern, msgids
                string = string.strip()

    def __init__(self, linter: PyLinter) -> None:
        super().__init__(linter)
        self.disable_entries = []
        self.enable_entries = []

    def load_configuration(self) -> None:
        for pattern, msgids in self.parse_argument_value(
            self.linter.config.disable_paths
        ):
            self.disable_entries.append(
                (
                    self.match_path,
                    pattern,
                    self.linter.disable,
                    msgids,
                    "--disable-paths",
                )
            )

        for pattern, msgids in self.parse_argument_value(
            self.linter.config.enable_paths
        ):
            self.enable_entries.append(
                (
                    self.match_path,
                    pattern,
                    self.linter.enable,
                    msgids,
                    "--enable-paths",
                )
            )

        for pattern, msgids in self.parse_argument_value(
            self.linter.config.disable_patterns
        ):
            self.disable_entries.append(
                (
                    self.match_pattern,
                    pattern,
                    self.linter.disable,
                    msgids,
                    "--disable-patterns",
                )
            )

        for pattern, msgids in self.parse_argument_value(
            self.linter.config.enable_paths
        ):
            self.enable_entries.append(
                (
                    self.match_pattern,
                    pattern,
                    self.linter.enable,
                    msgids,
                    "--enable-patterns",
                )
            )

    def process_tokens(self, tokens: list[TokenInfo]) -> None:
        for entries in [self.disable_entries, self.enable_entries]:
            for (
                match_func,
                pattern,
                xable_func,
                msgids,
                option_string,
            ) in entries:
                if match_func(pattern, self.linter.current_file):
                    lines = [
                        i for token in tokens for i in (token.start[0], token.end[0])
                    ]
                    lines = set(lines)
                    for msgid in msgids:
                        for line in lines:
                            try:
                                xable_func(msgid, "line", line + 1)
                            except (
                                exceptions.DeletedMessageError,
                                exceptions.MessageBecameExtensionError,
                            ) as e:
                                self.linter.add_message(
                                    "useless-option-value",
                                    args=(option_string, e),
                                    line=line,
                                )
                            except exceptions.UnknownMessageError:
                                self.linter.add_message(
                                    "unknown-option-value",
                                    args=(option_string, msgid),
                                    line=line,
                                )


def register_checker(linter: PyLinter, checker: XableMatchedPluginChecker) -> None:
    linter.register_checker(checker)

    original_process_tokens = linter.process_tokens

    def new_process_tokens(tokens: list[TokenInfo]):
        original_process_tokens(tokens)
        checker.process_tokens(tokens)

    linter.process_tokens = new_process_tokens


def register(linter: PyLinter) -> None:
    checker = XableMatchedPluginChecker(linter)
    register_checker(linter, checker)


def get_checker(linter: PyLinter, cls: type[BaseChecker]) -> BaseChecker | None:
    checkers = linter.get_checkers()
    checkers = filter(lambda checker: isinstance(checker, cls), checkers)
    checker = next(checkers, None)
    return checker


def load_configuration(linter: PyLinter) -> None:
    checker = get_checker(linter, XableMatchedPluginChecker)

    if checker:
        checker.load_configuration()
