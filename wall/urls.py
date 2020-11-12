from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("post", views.post),
    path("post/<int:msg_id>", views.comment),
]
