from django.db import models


class Subtitle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Decision(models.Model):
    date = models.DateField()
    headers = models.ManyToManyField(Subtitle)
    pdf = models.FileField(upload_to='secure')
    synopsis = models.TextField()

    def __str__(self):
        return self.synopsis
