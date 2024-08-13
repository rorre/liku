import random
from faker import Faker
from flask import Flask
import liku as e
from liku.html import html
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
    return html(
        """
        <Layout>
            <div class="flex flex-col gap-4">
                <HeaderRow />
                <GeneratedPost :n="5" :faker="faker" />
            </div>
        </Layout>
        """,
        globals(),
        locals(),
    )


@app.get("/post")
@component
def show_post():
    the_article = [e.p(children=p) for p in faker.paragraphs(64)]
    return html(
        """
        <Layout>
            <div class="flex flex-col gap-4">
                <h1 class="text-xl font-bold">{{ faker.sentence() }}</h1>
                <article>
                    {{ the_article }}
                </article>
            </div>
        </Layout>
        """,
        globals(),
        locals(),
    )


if __name__ == "__main__":
    app.run(debug=True)
