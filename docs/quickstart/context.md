# Passing State Deeply

In most cases, you only need to pass state between 2 components. However, there are cases where you need to either:

1. Pass state to components deep in the tree
2. Pass state to many different components, that could be both close and far away in the tree

Of course, you would still be able to achieve this by passing through props from one another, but this would cause
you to type in the state for every single component through the tree via props, which we call "prop drilling". To
avoid this, liku provides the same solution as what React does: using Context.

Context does this by providing data for all children components that are below it. Any child component below the
context provider will be able to get the current data using `use_context()` function. Therefore, all data can be
retrieved freely as long as there is a context object that is providing the value.

In general, context works just like this:

1. Create the context object, optionally with a default value
2. Provide the value of the context with `context.provide()` context manager (using `with` statement)
3. Use the value in child components

Let's see the example code:

```py title="context_demo.py"
from dataclasses import dataclass
import liku as e
from liku.context import Context, use_context


@dataclass
class User:
    name: str
    age: int
    role: str


UserContext = Context("user")


def Profile():
    user = use_context(UserContext)

    return e.div(
        props={"class_": "flex flex-col gap-2"},
        children=[
            e.p(children=str(user.age)),
            e.p(children=user.role),
            e.p(children=user.name),
        ],
    )


def Index():
    with UserContext.provide(User(name="Ren", age=20, role="admin")):
        return e.main(children=Profile())


print(Index())
```

Of course, this example don't really look very realistic as the context can be easily replaced with props
in this case. But you should keep note about how it is structured: Wrap all child components inside the
`with` statement, and use the context with `use_context`.
