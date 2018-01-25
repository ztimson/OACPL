from django.db import models
from django.contrib.auth.models import User


class ResetToken(models.Model):
    token = models.CharField(max_length=8)
    user = models.ForeignKey(User)
