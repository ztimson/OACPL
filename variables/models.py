from django.db import models


class Variable(models.Model):
    key = models.CharField(max_length=20, unique=True)
    value = models.TextField(blank=True, null=True)
    help_text = models.CharField(max_length=1000, blank=True, null=True)
