# HTML in Python

!!! warning "Experimental Feature"

    This feature is new and experimental. You may use this, but expect a lot of weirdness. If you find
    any issue, feel free to report to [GitHub Issues](https://github.com/rorre/liku/issues)

This is an alternative mode to write liku components. While using declarative mode works to define components,
it can be very overwhelming real quick, as well as not being very easy to read as the component grows bigger
and bigger. This mode fixes that issue by writing your component in HTML, while maintaining templating engine
features, much like JSX.

## Prerequisite

This feature requires `lxml` to be installed. To install the supported version, install the package with
`htm` extras:

```
pip install git+https://github.com/rorre/liku.git@main[htm]
```

## Visual Studio Code Extension

To aid developers on developing their app with Liku with HTML in Python mode, this extension for
Visual Studio Code exist. Currently, there is no ETA to release on marketplace, but you may see
the code and compile it yourself [here](https://github.com/rorre/liku-lsp).

Features:

- Completion on component names
- Completion on props
- Completion on `{{ expression }}` directive
- Completion on programmatic value props

However, there are a lot of caveats:

- **You must use triple backtick** inside `html()` for the completion to work.
- **All completions are taken on all scopes.** This means other function's locals will also be included.
- **No check for already filled in props.** This means you might be suggested already filled props.
- **No semantic tokens.** (aka syntax highlighting)
- **No type checks/linting.**

If you are using other editor, you may make use of the LSP inside `bundled/tools` directory.

## Feature Overview

Below is the code that we'll learn in this article. We'll explain all the features of across the following sections.
In general, all the html code will be done in a `html()` call, that can be imported from `liku.htm`

```py
from liku.htm import html

def Card(name: str, image: str | None):
    compact = image is None
    if compact:
        return html(
          """
          <div class="card card-compact">
              <p>{{ name }}</p>
          </div>
          """
        )
    return html(
        """
        <div class="card">
            <img :src="image" class="card-image" />
            <p>{{ name }}</p>
        </div>
        """
    )

def PeopleList(people: list[tuple[str, str | None]]):
    children = list(map(lambda p: html("""<Card :name="p[0]" :image="p[1]" />"""), people))
    # The following also works
    # children = list(map(lambda p: Card(p[0], p[1]), people))

    return html(
        """
        <div class="grid grid-cols-3 gap-2">
            {{ children }}
        </div>
        """
    )

people = [
  ("Ren", "https://avatars.githubusercontent.com/u/6541445?v=4"),
  ("Linus", None)
]
print(html(
    """
    <PeopleList :people="people />
    """
))
```

### Writing Components

A component is simply a function returning either a liku HTML element, a string, or `None`. You may also
return a list of any of the types mentioned earlier. To accomodate type check, you can import `HTMLNode`
from `liku.elements`.

```py
from liku.htm import html

def Example():
    return html("""<p>Hello world!</p>""")

print(html("""<Example />""")) # This will output <p>Hello world!</p>
```

When parsing your html, Liku will look through all your scoped variables, and call the function accordingly.

!!! note "Multiword Components"

    If your component has multiple word in the function name (such as `example_component()`), you can use
    `example-component` as well as `example_component` as the tag name. However, you should stick with snake
    case.

### Using Python Expression

Just like other templating engine, you are able to inject expression to print into the final HTML. In Liku,
this is done using `{{ expression }}` directive.

!!! danger

    This feature makes use of `eval()`. Please make sure all the expression are safe. Do not run user provided
    strings.

```py
from liku.htm import html

def Greet():
    name = "Liku"
    return html("""<p>Hello, {{ name }}!</p>""")

print(html("""<Greet />""")) # This will output <p>Hello, Liku!</p>
```

Liku will parse the html, find the directive and run the expression inside the directive. It will then replace
the directive with the result of the expression.

### Passing Props

All positional and keyword arguments are props in liku, **excluding variable arguments**. Therefore, all keys
must be the variable name of the function, and the value will be passed to the function call.

```py
from liku.htm import html

def Greet(name: str):
    return html("""<p>Hello, {{ name }}!</p>""")

print(html("""<Greet name="Liku" />""")) # This will output <p>Hello, Liku!</p>
```

!!! info

    You do not need type hints, but it would be best if you could.

Internally, liku will convert all props into a dict object, then spread it in the function call. For example,
the previous example will call the function like so: `Greet(**{"name": "Liku"})`, which is essentially the same
as calling `Greet(name="Liku")`. Therefore, the props order does not matter.

#### Catch-all Props

Sometimes you might need extra props that you don't care to list on. Maybe because there is too much, or you
simply just want to pass it to child or have special handling. You can do so using variable keyword arguments.

```py
from liku.htm import html
import liku as e

def ExampleForward(name: str, **kwargs: object):
    return e.p(
        props=kwargs,
        children=[
          f"Hello, {name}!"
        ]
    )

print(html("""<ExampleForward name="Liku" class="font-bold" />""")) # This will output <p class="font-bold">Hello, Liku!</p>
```

#### Programmatic Value

!!! danger

    This feature makes use of `eval()`. Please make sure all the expression are safe. Do not run user provided
    strings.

There are times where you might want the value of a prop be based on a variable or other data. You may do so by
prepending the key of the prop with a colon (`:`), and let the value be a Python expression.

```py
from liku.htm import html

def Greet(name: str):
    return html("""<p>Hello, {{ name }}!</p>""")

user_name = "Liku"
print(html("""<Greet :name="user_name" />""")) # This will output <p>Hello, Liku!</p>
```

Internally, Liku will parse through the props and run `eval()` on all of the value in such props.

### Control Flow

Outputting conditionally and looping through a list is a common problem during generation. You are
encouraged to split this logic outside of the `html()` call, as Liku itself does not have any logic
of conditional and recursion.

One way to achieve this is as follows:

```py
from dataclasses import dataclass
from liku.htm import html

@dataclass
class GroceryItem:
    name: str
    finished: bool

def Grocery(item: GroceryItem):
    # Run looping outside of html, saving the result...
    if item.finished:
        suffix = "(OK)"
    else:
        suffix = html("""<button>Finish</button>""")

    # ... then embed the result
    return html("""<li>{{ item.name }} {{ suffix }}</li>""")

def GroceriesList(items: list[GroceryItem]):
    # Run looping outside of html, saving the result...
    items_html = list(map(Grocery, items))
    return html(
        # ... then embed the result
        """
        <ul>{{ items_html }}</ul>
        """
    )

print(
    GroceriesList(
        [
            GroceryItem("Sample", True),
            GroceryItem("Sample 2", False),
        ]
    )
)

```
