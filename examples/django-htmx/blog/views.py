import random

from django.http import HttpRequest, HttpResponse
from faker import Faker
import liku as e
from blog.components import GeneratedPost, HeaderRow, Layout

faker = Faker()


def random_post(request: HttpRequest):
    return HttpResponse(GeneratedPost(random.randint(1, 10), faker))


def home(request: HttpRequest):
    return HttpResponse(
        Layout(
            e.div(
                props={"class_": "flex flex-col gap-4"},
                children=[
                    HeaderRow(),
                    GeneratedPost(5, faker),
                ],
            )
        )
    )


def show_post(request: HttpRequest):
    return HttpResponse(
        Layout(
            e.div(
                props={"class_": "flex flex-col gap-4"},
                children=[
                    e.h1(
                        props={"class_": "text-xl font-bold"}, children=faker.sentence()
                    ),
                    e.article(
                        children=[e.p(children=p) for p in faker.paragraphs(64)],
                    ),
                ],
            )
        )
    )
