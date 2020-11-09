import re
from django.db import models


class UserManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        EMAIL_FORMAT = re.compile(
            r"^[A-Za-z]+[-0-9A-Za-z._]*@[-0-9A-Za-z]{1,63}\.[A-Za-z]{1,63}$"
        )
        for key, value in form_data.items():
            if key in ("first_name", "last_name") and len(value) < 2:
                errors[key] = "Names must be at least two characters"
            elif key == "email" and not EMAIL_FORMAT.match(form_data["email"]):
                errors["email"] = "Invalid email address"
            elif key == "password":
                if value != form_data["confirm_pw"]:
                    errors[
                        "pass_match"
                    ] = "Password and password confirmation don't match"
                if len(value) < 8:
                    errors["pass_length"] = "Password must be at least 8 characters"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
