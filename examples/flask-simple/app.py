import random
from faker import Faker
from flask import Flask
import liku as e

from liku.integrations.flask import component
from components import HeaderRow, Layout, GeneratedPost

app = Flask(__name__)
faker = Faker()


@app.get("/random")
@component
def random_post():
    return GeneratedPost(random.randint(1, 10), faker)


@app.get("/")
@component
def home():
    return Layout(
        e.div(
            props={"class_": "flex flex-col gap-4"},
            children=[
                HeaderRow(),
                GeneratedPost(5, faker),
            ],
        )
    )


@app.get("/post")
@component
def show_post():
    return Layout(
        e.div(
            props={"class_": "flex flex-col gap-4"},
            children=[
                e.h1(props={"class_": "text-xl font-bold"}, children=faker.sentence()),
                e.article(
                    children=[e.p(children=p) for p in faker.paragraphs(64)],
                ),
            ],
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
