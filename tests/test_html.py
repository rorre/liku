import html
from typing import Type
import pytest
import liku as e
from liku.elements import HTMLElement


def test_generic():
    component = e.GenericComponent.create("sample")
    assert str(component()) == "<sample></sample>"
    assert component.__name__ == "sample"
    assert (
        str(component(props={"example": "props"}))
        == '<sample example="props"></sample>'
    )
    assert str(component(children="text")) == "<sample>text</sample>"
    assert (
        str(component(props={"example": "props"}, children="text"))
        == '<sample example="props">text</sample>'
    )


def test_fragment():
    assert str(e.Fragment()) == ""
    assert str(e.Fragment(props={"unused": "props"})) == ""
    assert str(e.Fragment(children="test")) == "test"


def test_props():
    # Normal props + _ suffix
    component = e.img(props={"src": "https://google.com", "class_": "mx-auto"})
    assert component.format_props() == 'src="https://google.com" class="mx-auto"'

    # Non-str props
    component = e.iframe(
        props={
            "height": 1,
            "allowfullscreen": True,
            "allowtransparency": False,
        }
    )
    assert (
        component.format_props()
        == 'height="1" allowfullscreen="true" allowtransparency="false"'
    )

    # HTML escape all values
    component = e.a(props={"href": '"<img src="" onload="alert(1)" />'})
    assert (
        component.format_props()
        == 'href="&quot;&lt;img src=&quot;&quot; onload=&quot;alert(1)&quot; /&gt;"'
    )

    # Invalid data type
    component = e.a(props={"invalid": []})  # type: ignore
    with pytest.raises(TypeError):
        component.format_props()


def test_render_child():
    assert e.a(children="text").render_child() == "text"

    child = e.p(children="Hello world!")
    assert e.div(children=child).render_child() == child.render()

    child2 = e.div(children=e.p(children="Recursive"))
    assert e.div(children=[child, child2]).render_child() == (
        child.render() + child2.render()
    )

    text = "not a component"
    assert e.div(
        children=[child, child2, text],
    ).render_child() == (child.render() + child2.render() + text)

    # Safe option
    unsafe_text = '<img src="" onload="alert(1)" />'
    assert e.div(children=unsafe_text, safe=True).render_child() == unsafe_text
    assert e.div(children=unsafe_text).render_child() == html.escape(unsafe_text)

    # Safe at child, so it should be OK
    assert (
        e.div(children=e.p(children=unsafe_text), safe=True).render_child()
        == f"<p>{html.escape(unsafe_text)}</p>"
    )


def test_h():
    assert (
        e.h(
            "a",
            {"href": "https://google.com"},
            children=e.h("strong", children="h() function"),
        ).render()
        == e.a(
            props={"href": "https://google.com"},
            children=e.strong(children="h() function"),
        ).render()
    )


def test_void_element():
    elems: list[Type[HTMLElement]] = [
        e.area,
        e.base,
        e.br,
        e.col,
        e.embed,
        e.hr,
        e.img,
        e.input,
        e.link,
        e.meta,
        e.param,
        e.source,
        e.track,
        e.wbr,
    ]

    for elem in elems:
        assert (
            str(elem(props={"class_": "sample"}, children="not used"))
            == f'<{elem.__name__} class="sample" />'
        )
