from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("random", views.random_post, name="random"),
    path("post", views.show_post, name="post"),
]
