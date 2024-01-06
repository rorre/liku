# Introduction

Liku is a library to render HTML, inspired by modern Web Development.

## Quickstart

- Install the package first! (PyPI soon)
- Start working by importing the library: `import liku as e`
- Write your components! See example below

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

## Features

- **Python**: It literally is just Python, everything is represented in Python
- **Statically Typed**: Every single component is statically typed, even the props/attributes
- **Zero dependencies**: Unless you add integrations support, there is no added dependencies whatsoever
- **Fast**: There is no I/O logic, just traversing through the tree (benchmark soon)

## Optional Dependencies

- `liku[flask]`: Flask >= 1.1.0, < 4.0. Essentially all stable versions

## Examples

Examples available at [examples directory](https://github.com/rorre/liku/tree/main/examples)
