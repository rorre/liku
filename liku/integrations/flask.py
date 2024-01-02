from functools import wraps
from typing import Callable, Mapping, Sequence, Tuple, Union
from flask import Response
from liku.elements import HTMLElement


HeadersValue = Union[
    Mapping[str, str],
    Sequence[Tuple[str, str]],
]

ResponseReturnValue = (
    Tuple[HTMLElement, HeadersValue]
    | Tuple[HTMLElement, int]
    | Tuple[HTMLElement, int, HeadersValue]
    | HTMLElement
)
RouteCallable = Callable[..., ResponseReturnValue]


def component_response[T: ResponseReturnValue, **P](
    f: Callable[P, T],
) -> Callable[P, Response]:
    """Converts view function to automatically convert Liku's HTML Elements to Flask's Response."""

    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Response:
        result = f(*args, **kwargs)

        if isinstance(result, HTMLElement):
            return Response(str(result), content_type="text/html")

        html_str = str(result[0])
        headers: HeadersValue = {}
        status = 200
        if len(result) == 2:
            if isinstance(result[1], int):
                status = result[1]
            else:
                headers = result[1]
        else:
            status = result[1]
            headers = result[2]

        return Response(
            html_str,
            headers=headers,
            status=status,
            content_type="text/html",
        )

    return wrapper
