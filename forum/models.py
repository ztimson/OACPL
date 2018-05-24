from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField


class Thread(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    thread = models.ForeignKey(Thread, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    question = HTMLField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    reply = HTMLField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
