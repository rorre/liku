import random
from flask import Flask, Response
import liku as e
from faker import Faker


app = Flask(__name__)
faker = Faker()


def to_html(el: e.HTMLElement):
    return Response(str(el), content_type="text/html")


def GeneratedPost(n: int):
    return e.div(
        props={"id": "posts", "class_": "flex flex-col gap-4"},
        children=[Card(faker.sentence(), faker.paragraphs()) for _ in range(n)],
    )


def Layout(children: e.HTMLNode):
    return e.html(
        children=[
            e.head(
                children=[
                    e.title(children="Hello World!"),
                    e.meta(props={"charset": "utf-8"}),
                    e.meta(
                        props={
                            "name": "viewport",
                            "content": "width=device-width, initial-scale=1",
                        }
                    ),
                    e.script(props={"src": "https://cdn.tailwindcss.com"}),
                    e.script(props={"src": "https://unpkg.com/htmx.org@1.9.10"}),
                ]
            ),
            e.body(
                children=[
                    e.div(
                        props={"class_": "container mx-auto pt-8"},
                        children=children,
                    )
                ]
            ),
        ]
    )


def Card(title: str, description: str):
    return e.div(
        {"class_": "rounded-md border p-4"},
        children=[
            e.strong(children=title),
            e.p(children=description),
            e.a(
                props={
                    "href": "https://google.com",
                    "class_": "underline text-blue-500 hover:cursor-pointer",
                },
                children="Read More",
            ),
        ],
    )


@app.get("/random")
def random_post():
    return to_html(GeneratedPost(random.randint(1, 10)))


@app.get("/")
def home():
    return to_html(
        Layout(
            e.div(
                props={"class_": "flex flex-col gap-4"},
                children=[
                    e.div(
                        props={
                            "class_": "flex flex-row gap-4 justify-between items-center"
                        },
                        children=[
                            e.h1(
                                props={"class_": "text-xl font-bold"},
                                children="My Blog!",
                            ),
                            e.button(
                                props={
                                    "class_": "rounded-md px-4 py-2 border-blue-500 border",
                                    "hx-get": "/random",
                                    "hx-target": "#posts",
                                    "hx-swap": "outerHTML",
                                },
                                children="Randomize Post",
                            ),
                        ],
                    ),
                    GeneratedPost(5),
                ],
            )
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
