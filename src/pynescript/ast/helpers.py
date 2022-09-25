from __future__ import annotations

from pynescript.ast.types import AST


def iter_fields(node: AST):
    return node.iter_fields()


def iter_child_nodes(node):
    for _name, field in iter_fields(node):
        if isinstance(field, AST):
            yield field
        elif isinstance(field, list):
            for item in field:
                if isinstance(item, AST):
                    yield item


def walk(node):
    from collections import deque

    todo = deque([node])
    while todo:
        node = todo.popleft()
        todo.extend(iter_child_nodes(node))
        yield node


def _dump_value_impl(value, indent: str = "", depth: int = 0):
    if isinstance(value, AST):
        return _dump_impl(value, indent=indent, depth=depth)
    elif isinstance(value, list) and len(value) > 0:
        lines = []
        lines.append("[")
        for subvalue in value:
            lines.append(
                f"{indent * (depth + 1)}{_dump_value_impl(subvalue, indent=indent, depth=depth + 1)},"
            )
        lines.append(f"{indent * depth}]")
        return "\n".join(lines)
    else:
        return f"{value!r}"


def _dump_impl(node: AST, indent: str = "", depth: int = 0):
    class_name = node.__class__.__name__
    class_params = dict(iter_fields(node))
    if indent and len(class_params) > 0:
        lines = []
        lines.append(f"{class_name}(")
        for name, value in class_params.items():
            lines.append(
                f"{indent * (depth + 1)}{name}={_dump_value_impl(value, indent=indent, depth=depth + 1)},"
            )
        lines.append(f"{indent * depth})")
        return "\n".join(lines)
    else:
        class_params = [f"{name}={value!r}" for name, value in class_params.items()]
        class_params = ", ".join(class_params)
        return f"{class_name}({class_params})"


def dump(node: AST, indent: int | str | None = None) -> str:
    if indent is None:
        indent = 0
    if isinstance(indent, int):
        indent = " " * indent
    return _dump_impl(node, indent=indent)


def unparse(node: AST) -> str:
    from pynescript.ast.node_visitors import Unparser

    unparser = Unparser()
    return unparser.visit(node)


def literal_eval(node_or_string: str | AST):
    raise NotImplementedError()
