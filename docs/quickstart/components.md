# Creating Liku Component

To create a Liku component, you need to have the library installed. Follow the [installation guide](installation.md) to get started.

## Overview

A Liku component is just an instance of an abstract class named `HTMLElement`. In general, you would not need to extend this class,
as Liku already provide all wrappers for every single HTML node available in `liku` namespace.

Each `HTMLElement` has two arguments in its class init: `props` and `children`. `props` is the attributes for that HTML tag. It is
the same concept as the one in React/Vue/Solid encosystem. `children` is the child HTML nodes of that attribute, that is the elements
between the opening and closing tag.

For example, take a look at the HTML code below:

```html
<div class="mx-auto container">
  <p>Hello world!</p>
</div>
```

In the case for `<div>` tag, `class="mx-auto container"` is the `props`, and `<p>Hello world!</p>` is the children.

!!! note

    Some props would have `_` prefix, this is because it conflicts with Python keyword, so adding `_` is necessary to avoid Python
    syntax errors.

## Creating

To create a new component, simply call the html tag that you want, and provide in the props and children. Let's try to convert the above
example to how Liku would represent it:

```python
import liku as e

container = e.div(
    props={"class_": "mx-auto container"}
    children=[
        e.p(children="Hello world!")
    ]
)
print(container)
```

## Composability through functions

The component code can grow really big as your page or component grow much bigger, and with the default of PEP8 to use 4 spaces, it can
get really stretched horizontally really quick! So, it is wise for you to be able to compose your components into multiple separate
components.

Making functional components is just like how you would in React or Solid, you create a function, have the arguments as its props, then
return the html component. To use the component, simply call the functional component and pass it to the parent component's children.
Very simple, isn't it?

Let's make a component just like this one:

<figure>
    <img src="https://i.imgur.com/TUWTECN.png)" />
</figure>

Here is the HTML code for the component:

```html
<div class="bg-white rounded-md border flex flex-row gap-16 py-4 px-8 max-w-lg">
  <div class="flex flex-col gap-4 items-center justify-center flex-none">
    <img
      src="https://avatars.githubusercontent.com/u/6541445?v=4"
      class="rounded-full w-32 aspect-square"
    />
    <p>Ren</p>
  </div>

  <div class="flex flex-col gap-2 justify-between py-8">
    <p class="font-light">
      Local cat meowing at terminal. I love other cats too!
    </p>

    <div class="grid grid-cols-2">
      <a class="text-blue-500 underline">Twitter</a>
      <a class="text-blue-500 underline">GitHub</a>
    </div>
  </div>
</div>
```

Let's split this into 3 components: Card, UserPreview, UserDetails

```python
import liku as e
from dataclasses import dataclass

@dataclass
class User:
    avatar: str
    name: str
    bio: str
    socials: dict[str, str]

def UserPreview(avatar: str, name: str):
    return e.div(
        props={"class_": "flex flex-col gap-4 items-center justify-center flex-none"},
        children=[
            e.img(props={
                "src": avatar,
                "class_": "rounded-full w-32 aspect-square"
            }),
            e.p(children=name),
        ]
    )

def UserDetails(bio: str, socials: dict[str, str]):
    return e.div(
        props={"class_": "flex flex-col gap-2 justify-between py-8"},
        children=[
            e.p(
                props={"class_": "font-light"},
                children=bio
            ),

            e.div(
                props={"class_": "grid grid-cols-2"},
                children=[
                    e.a(
                        props={"href": link, "class_": "text-blue-500 underline"},
                        children=social
                    ) for social, link in socials.items()
                ]
            )
        ]
    )

def Card(user: User):
    return e.div(
        props={"class_": "bg-white rounded-md border flex flex-row gap-16 py-4 px-8 max-w-lg"},
        children=[
            UserPreview(user.avatar, user.name),
            UserDetails(user.bio, user.socials)
        ]
    )

ren = User(
    avatar="https://avatars.githubusercontent.com/u/6541445?v=4",
    name="Ren",
    bio="Local cat meowing at terminal. I love other cats too!",
    socials={
        "Twitter": "https://twitter.com",
        "GitHub": "https://github.com/rorre"
    }
)

print(Card(ren))
```

As you can see, it is much more maintainable and easily customizable now that it has been splitted.

Now that you know how to build components, continue on how to integrate Liku to web frameworks in the next page.
