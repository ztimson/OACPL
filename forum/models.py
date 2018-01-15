from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField


class Thread(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    thread = models.ForeignKey(Thread)
    title = models.CharField(max_length=255)
    question = HTMLField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    reply = HTMLField()
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
