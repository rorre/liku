import liku as e
from faker import Faker
from liku.htm import html


def HeaderRow():
    return html(
        """
        <div class="flex flex-row gap-4 justify-between items-center">
            <h1 class="text-xl font-bold">My Blog!</h1>
            <button
                class="rounded-md px-4 py-2 border-blue-500 border"
                hx-get="/random"
                hx-target="#posts"
                hx-swap="outerHTML"
            >Randomize Post</button>
        </div>   
        """
    )


def GeneratedPost(n: int, faker: Faker):
    posts = [
        html(
            """<Card :title="faker.sentence()" :description="'\n'.join(faker.paragraphs())" />"""
        )
        for _ in range(n)
    ]
    return html(
        """
        <div id="posts" class="flex flex-col gap-4">
            {{ posts }}
        </div>
        """
    )


def Layout(children: e.HTMLElement | str | list):
    return html(
        """
        <html lang="en">
            <head>
                <title>Hello World!</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <script src="https://cdn.tailwindcss.com"></script>
                <script src="https://unpkg.com/htmx.org@1.9.10"></script>
            </head>
            <body>
                <div class="container mx-auto pt-8">
                    {{ children }}
                </div>
            </body>
        </html>         
        """
    )


def Card(title: str, description: str):
    return html(
        """
        <div class="rounded-md border p-4">
            <strong>{{ title }}</strong>
            <p>{{ description }}</p>
            <a href="post" class="underline text-blue-500 hover:cursor-pointer">
                Read More
            </a>
        </div>
        """
    )
