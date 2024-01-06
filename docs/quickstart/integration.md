# Integrations With Web Frameworks

After you have known how to create components, it is time to integrate with your beloved web frameworks!
Below are guides to get you started to using Liku with various web frameworks:

## Django

Support is available out of the box. You can return the component in your view function with HttpResponse:

```py title="views.py"
import liku as e
from django.http import HttpRequest, HttpResponse

def hello_world(request: HttpRequest):
    return HttpResponse(
        e.div(
            props={"class_": "mx-auto container"},
            children=e.p(children="Hello world!")
        )
    )
```

Django will automatically convert the component to HTML.

## Flask

Liku provides the decorator `@component` in `liku.integrations.flask` to automatically convert
Liku components to Flask response.

```py title="app.py"
import liku as e
from liku.integrations.flask import component

# ...

@app.get("/")
@component
def hello_world():
    return e.div(
        props={"class_": "mx-auto container"},
        children=e.p(children="Hello world!")
    )
```

Just like regular Flask view, you are still able to return your status code and headers in the response
as tuple as well. What matters is that the first value of return must be the component.

## Starlette / FastAPI

Support is available out of the box. You can return the component in your view function with HTMLResponse

```py title="app.py"
import liku as e

# ...

@app.get("/", response_class=HTMLResponse)
async def hello_world():
    return e.div(
        props={"class_": "mx-auto container"},
        children=e.p(children="Hello world!")
    )
```

Starlette or FastAPI convert the component to HTML.
