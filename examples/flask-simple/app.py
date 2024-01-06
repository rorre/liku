import random
from flask import Flask
import liku as e

from liku.integrations.flask import component
from components import Layout, GeneratedPost

app = Flask(__name__)


@app.get("/random")
@component
def random_post():
    return GeneratedPost(random.randint(1, 10))


@app.get("/")
@component
def home():
    return Layout(
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


if __name__ == "__main__":
    app.run(debug=True)
