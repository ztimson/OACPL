from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class Post(models.Model):
    topic = models.ForeignKey(Thread)
    title = models.CharField(max_length=255)
    question = models.TextField()
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    reply = models.TextField()
    creator = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
