from django.db import models
from login.models import User


class MessageManager(models.Manager):
    def make_post(self, msg, user_id):
        Message.objects.create(user_id=User.objects.get(id=user_id), message=msg)


class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = MessageManager()


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    message_id = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
