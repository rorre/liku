from flask import Flask
import pytest
import liku as e
from liku.integrations.flask import component


@pytest.fixture()
def app():
    app = Flask("liku")
    with app.app_context():
        yield app


def test_integration(app):
    elem = e.div(children=e.p(props={"class_": "font-bold"}, children="Hello world!"))

    @component
    def f():
        return elem

    response = f()
    assert response.get_data(True) == str(elem)
    assert len(response.headers) == 2
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

    @component
    def f_with_status():
        return elem, 403

    response = f_with_status()
    assert response.get_data(True) == str(elem)
    assert len(response.headers) == 2
    assert response.status_code == 403
    assert response.content_type == "text/html; charset=utf-8"

    @component
    def f_with_status_headers():
        return elem, 403, {"X-Example": "Hello"}

    response = f_with_status_headers()
    assert response.get_data(True) == str(elem)
    assert len(response.headers) == 3
    assert response.headers.get("X-Example") == "Hello"
    assert response.status_code == 403
    assert response.content_type == "text/html; charset=utf-8"

    @component
    def f_with_headers():
        return elem, {"X-Example": "Hello"}

    response = f_with_headers()
    assert response.get_data(True) == str(elem)
    assert len(response.headers) == 3
    assert response.headers.get("X-Example") == "Hello"
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"

    @component
    def f_with_headers_tuple():
        return elem, [("X-Example", "Hello")]

    response = f_with_headers_tuple()
    assert response.get_data(True) == str(elem)
    assert len(response.headers) == 3
    assert response.headers.get("X-Example") == "Hello"
    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
