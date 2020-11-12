from django.shortcuts import render, redirect
from login.models import User
from .models import Message


def index(request):
    context = {
        "this_user": User.objects.get(id=request.session["id"]),
        "all_messages": Message.objects.all(),
    }
    return render(request, "wall.html", context)


def post(request):
    if request.method == "POST":
        Message.objects.make_post(
            user_id=request.session["id"], msg=request.POST["message"]
        )
    return redirect("/wall")
