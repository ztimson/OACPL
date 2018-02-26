from django.db import models
from django.contrib.auth.admin import User


class Attachment(models.Model):
    file = models.FileField(upload_to='PressRelease')

    def name(self):
        return self.file.name.replace('PressRelease/', '')

    def __str__(self):
        return self.file.name


class PressRelease(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    attachments = models.ManyToManyField(Attachment)

    def __str__(self):
        return self.title
