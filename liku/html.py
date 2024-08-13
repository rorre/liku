import re
from typing import Any, get_type_hints
from liku import HTMLElement, HTMLNode, __all__ as liku_exports
from liku.elements import h
from lxml.etree import _Element as Element, _Attrib as Attrib, XML
from lxml.html import fragment_fromstring, tostring, XHTMLParser

CODE_RE = re.compile(r"{{(.+)}}")


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
        if isinstance(result, list):
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

    props = {**props, "children": children}

    func = None
    if globals:
        func = globals.get(tag_name)

    if locals and not func:
        func = locals.get(tag_name)

    if not func:
        raise Exception(f"Cannot find component for tag '{elem.tag}'")

    hints = get_type_hints(func)
    # return_type = hints.pop("return")
    # if return_type not in (HTMLElement, str, list):
    #     raise TypeError(f"Return type of component '{elem.tag}' must be HTMLElement | str | list, got '{return_type}'")

    validated_props: dict[str, Any] = {}
    missing_props: set = set()
    for k in hints.keys():
        if k not in props:
            missing_props.add(k)
            continue

        if not isinstance(props[k], hints[k]):
            raise TypeError(f"Props type mismatch for '{k}': expected '{hints[k]}', got '{type(props[k])}'")

        validated_props[k] = props[k]

    if missing_props:
        raise ValueError(f"Missing {len(missing_props)} props: {','.join(missing_props)}")

    return func(**validated_props)


def html(entity: str, globals: dict | None = None, locals: dict | None = None):
    parser = XHTMLParser(recover=True)
    try:
        root = fragment_fromstring(entity, parser=parser)
    except AssertionError:
        root = XML(entity, parser)
    return _element_to_html(root, globals, locals)
