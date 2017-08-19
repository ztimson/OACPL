from django.db import models
from django.contrib.auth.admin import User
from django.utils.timezone import now


class Newsletter(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    publish = models.DateTimeField(default=now())
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)

    def __str__(self):
        return ''
