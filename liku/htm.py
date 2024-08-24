from collections.abc import Iterable
import inspect
import re
from typing import Any
from liku import HTMLNode, __all__ as liku_exports
from liku.elements import h
from lxml.etree import _Element as Element, _Attrib as Attrib, XML
from lxml.html import fragment_fromstring, XHTMLParser

CODE_RE = re.compile(r"{{(.+?)}}")


def _process_text_code(
    text: str,
    globals: dict | None = None,
    locals: dict | None = None,
):
    results: list[HTMLNode] = []
    while match := CODE_RE.search(text):
        previous = text[: match.start()]
        if previous:
            results.append(previous)

        result = eval(match.group(1), globals, locals)
        if isinstance(result, Iterable):
            results.extend(result)
        else:
            results.append(result)
        text = text[match.end() :]

    if text:
        results.append(text)
    return results


def _resolve_props(
    props: Attrib,
    globals: dict | None = None,
    locals: dict | None = None,
) -> dict[str, Any]:
    resolved_props: dict[str, str] = {}
    for k, v in props.iteritems():
        actual_value = v
        if k.startswith(":"):
            # I think there needs to be a better way for this
            k = k[1:]
            actual_value = eval(v, globals, locals)

        resolved_props[k] = actual_value
    return resolved_props


def _element_to_html(
    elem: Element,
    globals: dict | None = None,
    locals: dict | None = None,
) -> HTMLNode:
    tag_name = elem.tag.replace("-", "_")
    props = _resolve_props(elem.attrib, globals, locals)

    children: list[HTMLNode] = []
    if elem.text:
        children.extend(_process_text_code(elem.text, globals, locals))

    for child in elem:
        children.append(_element_to_html(child, globals, locals))
        if child.tail:
            children.extend(_process_text_code(child.tail, globals, locals))

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

    try:
        root = fragment_fromstring(entity, parser=parser)
    except AssertionError:
        root = XML(entity, parser)

    return _element_to_html(root, previous_frame.f_globals, previous_frame.f_locals)
