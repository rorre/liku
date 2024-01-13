from liku.context import Context, use_context

import pytest


def test_context():
    ctx = Context("testcontext")
    with pytest.raises(LookupError):
        ctx.get()

    with ctx.provide("sample"):
        assert ctx.get() == "sample"
        assert use_context(ctx) == "sample"

    with pytest.raises(LookupError):
        ctx.get()


def test_default():
    ctx = Context("testcontext", "defaultvalue")
    assert ctx.get() == "defaultvalue"

    with ctx.provide("sample"):
        assert ctx.get() == "sample"
        assert use_context(ctx) == "sample"

    assert ctx.get() == "defaultvalue"
