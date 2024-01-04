from django.http import HttpResponse

from liku.elements import HTMLElement


class HttpLikuResponse(HttpResponse):
    def __init__(self, content: HTMLElement, *args, **kwargs):
        return super().__init__(str(content), *args, **kwargs)
