import random

from django.http import HttpRequest, HttpResponse
import liku as e
from blog.components import GeneratedPost, Layout


def random_post(request: HttpRequest):
    return HttpResponse(GeneratedPost(random.randint(1, 10)))


def home(request: HttpRequest):
    return HttpResponse(
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
