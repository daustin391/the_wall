import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request, "index.html")


def success_redirect(request, user_id):
    request.session["id"] = user_id
    return redirect("/success")


def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
        else:
            password = request.POST["password"]
            hashword = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                password=hashword,
            )
            return success_redirect(request, User.objects.last().id)
    return redirect("/")


def login(request):
    if request.method == "POST":
        this_user = User.objects.filter(email=request.POST["email"])
        if this_user and bcrypt.checkpw(
            request.POST["password"].encode(), this_user[0].password.encode()
        ):
            return success_redirect(request, this_user[0].id)
        else:
            messages.error(request, "Invalid login")

    return redirect("/")


def success(request):
    if "id" in request.session.keys():
        context = {"this_user": User.objects.get(id=request.session["id"])}
        return render(request, "success.html", context)
    else:
        return redirect("/")


def logout(request):
    request.session.flush()
    return redirect("/")
