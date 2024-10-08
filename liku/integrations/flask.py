from functools import wraps
from typing import Callable, Mapping, Sequence, Tuple, Union
from flask import Response, make_response
from liku.elements import HTMLNode, HTMLElement


HeadersValue = Union[
    Mapping[str, str],
    Sequence[Tuple[str, str]],
]

ResponseReturnValue = (
    Tuple[HTMLNode | Response, HeadersValue]
    | Tuple[HTMLNode | Response, int]
    | Tuple[HTMLNode | Response, int, HeadersValue]
    | HTMLNode
    | Response
)
RouteCallable = Callable[..., ResponseReturnValue]


def component[
    T: ResponseReturnValue, **P
](f: Callable[P, T],) -> Callable[P, Response]:
    """Converts view function to automatically convert Liku's HTML Elements to Flask's Response."""

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Response:
        result = f(*args, **kwargs)

        if isinstance(result, HTMLElement):
            return make_response(str(result))
        if isinstance(result, Response):
            return result

        component, *rest = result
        return make_response(str(component), *rest)

    return wrapper
