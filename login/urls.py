from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("wall/", include("wall.urls")),
    path("logout", views.logout),
]
