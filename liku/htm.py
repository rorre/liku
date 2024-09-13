from collections import OrderedDict, deque
import inspect
from typing import Any
from liku import HTMLNode, __all__ as liku_exports
from liku._utils import random_str
from liku.elements import h
from lxml.etree import _Element as Element, _Attrib as Attrib, XML
from lxml.html import fragment_fromstring, XHTMLParser

__LIKU_IDENT__ = "#LIKU_TOREPLACE"


def _find_first_code(text: str):
    stack = 0
    brackets_buf = deque("", maxlen=2)
    buf = ""
    is_inside_block = False

    for c in text:
        brackets_buf.append(c)
        if is_inside_block:
            buf += c

        if "".join(brackets_buf) == "{{":
            stack += 1
            brackets_buf.clear()
            if stack == 1:
                buf = "{{"
        elif "".join(brackets_buf) == "}}":
            stack -= 1
            brackets_buf.clear()

            if stack == 0:
                return buf
            stack = max(stack, 0)

        is_inside_block = stack > 0


def _process_text_code(
    text: str,
    globals: dict | None = None,
    locals: dict | None = None,
):
    replacement_mapping: dict[str, Any] = OrderedDict()

    while match := _find_first_code(text):
        result = eval(match[2:-2], globals, locals)
        identifier = __LIKU_IDENT__ + random_str(64)
        replacement_mapping[identifier] = result
        text = text.replace(match, identifier)

    return text, replacement_mapping


def _resolve_replacement(
    text: str,
    mapping: dict[str, Any],
):
    resolved_childrens = []
    while text.find(__LIKU_IDENT__) != -1:
        start_idx = text.find(__LIKU_IDENT__)
        end_idx = start_idx + len(__LIKU_IDENT__) + 64
        if start_idx > 0:
            resolved_childrens.append(text[:start_idx])

        ident = text[start_idx:end_idx]
        if ident in mapping:
            value = mapping.pop(ident)
            resolved_childrens.append(value)
        else:
            resolved_childrens.append(ident)
        text = text[end_idx:]

    if text:
        resolved_childrens.append(text)
    return resolved_childrens


def _resolve_props(
    props: Attrib,
    globals: dict | None = None,
    locals: dict | None = None,
) -> dict[str, Any]:
    resolved_props: dict[str, str] = {}
    for k, v in props.iteritems():
        if v.startswith(__LIKU_IDENT__):
            raise ValueError(
                "You are using template variable inside a dynamic props. Please remove the brackets."
            )

        actual_value = v
        if k.startswith(":"):
            # I think there needs to be a better way for this
            k = k[1:]
            actual_value = eval(v, globals, locals)

        resolved_props[k] = actual_value
    return resolved_props


def _element_to_html(
    elem: Element,
    mapping: dict[str, Any],
    globals: dict | None = None,
    locals: dict | None = None,
) -> HTMLNode:
    tag_name = elem.tag.replace("-", "_")
    props = _resolve_props(elem.attrib, globals, locals)

    children: list[Any] = []
    if elem.text:
        children.extend(_resolve_replacement(elem.text, mapping))

    for child in elem:
        children.append(_element_to_html(child, mapping, globals, locals))
        if child.tail:
            children.extend(_resolve_replacement(child.tail, mapping))

    if tag_name in liku_exports:
        return h(tag_name, props, children)  # type: ignore

    func = None
    if locals:
        func = locals.get(tag_name)

    if globals and not func:
        func = globals.get(tag_name)

    if not func:
        return h(tag_name, props, children)  # type: ignore

    func_argspec = inspect.getfullargspec(func)
    if "children" in (*func_argspec.args, *func_argspec.kwonlyargs):
        props = {**props, "children": children}

    return func(**props)


def html(entity: str):
    previous_frame = inspect.stack(2)[1].frame
    parser = XHTMLParser(recover=True)

    entity, mapping = _process_text_code(
        entity, previous_frame.f_globals, previous_frame.f_locals
    )

    try:
        root = fragment_fromstring(entity, parser=parser)
    except AssertionError:
        root = XML(entity, parser)

    return _element_to_html(
        root,
        mapping,
        previous_frame.f_globals,
        previous_frame.f_locals,
    )
