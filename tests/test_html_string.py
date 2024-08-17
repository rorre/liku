from liku.htm import html


def test_self_closing():
    assert (
        str(html("""<div class="something" />"""))
        == """<div class="something"></div>"""
    )
    assert (
        str(html("""<area class="something" />""")) == """<area class="something" />"""
    )


def test_custom():
    assert (
        str(html("""<custom tag="yeah!"><p>hello</p></custom>"""))
        == """<custom tag="yeah!"><p>hello</p></custom>"""
    )


def test_normal():
    assert (
        str(html("<div><div>hello world!</div><p>i'm normal</p></div>"))
        == "<div><div>hello world!</div><p>i&#x27;m normal</p></div>"
    )


def example():
    return html("<p>yo</p>")


def overshadowed():
    raise Exception("Should never happen")


def test_resolve_component():
    local = lambda: html("<p>sup</p>")  # noqa: E731

    def overshadowed():
        return html("<p>overriden</p>")

    assert str(html("<local />")) == "<p>sup</p>"
    assert str(html("<example />")) == "<p>yo</p>"
    assert str(html("<overshadowed />")) == "<p>overriden</p>"


def test_resolve_props():
    example_var = "working"
    assert (
        str(html("""<div :example="example_var"></div>"""))
        == """<div example="working"></div>"""
    )


def test_resolve_inline():
    example_var = "working"
    assert (
        str(html("""<div>{{ example_var }} okay</div>"""))
        == """<div>working okay</div>"""
    )
