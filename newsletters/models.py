from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone

from tinymce.models import HTMLField


class Newsletter(models.Model):
    body = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    publish = models.DateTimeField(default=timezone.now)
    sent = models.BooleanField(default=False)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.subject


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
