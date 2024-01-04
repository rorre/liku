import liku as e
from faker import Faker

faker = Faker()


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
