# Introduction

Liku is a library to render HTML, inspired by modern Web Development.

## Quickstart

- Install the package first! (PyPI soon)
- Start working by importing the library: `import liku as e`

### Simple Component

```python
import liku as e

def Card(title: str, description: str):
    return e.div(
        props={"class_": "rounded-md border p-4"},
        children=[
            e.strong(children=title),
            e.p(children=description),
        ],
    )

print(Card("Hello", "world!"))
# <div class="rounded-md border p-4"><strong >Hello</strong><p >world!</p></div>
```

## Motivation

Templating engine always uses some sort of custom format, whether it be Jinja, Django's templating, or anything else. These are powerful tools,
but after going back from the time where I keep writing React code, something clicks in me: "I like extending JS with HTML". So, I decided
to do just that in this library.

The benefit of this project is that I have the full power of Python, while still being able to reflect my front-end code at the same time.
This way, not only I can benefit from Python's LSP, I have full control of what is executed, so integrating with database is easier.

The ideas are as follows:

- Allow full LSP and typed nature of representing HTML
- Easily compose components into each own function (very useful for maintainability, and with HTMX on the rise, this makes even more sense)
- Keep library as simple as possible

## Future

Considering there is already the equivalent of `h()` function in JS ecosystem, there is a plan to write own JSX system in Python, hopefully
with LSP support as well. This would mean that both HTML and Python can be very easily represented in the same space, making SSR rendered
apps more powerful to use and less of a headache to manage.

## Examples

Examples available at [examples directory](./examples)
