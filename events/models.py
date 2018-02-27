from django.db import models

from tinymce import HTMLField


class Attendees(models.Model):
    name = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, null=True, blank=True)
    description = HTMLField()
    max_attendees = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    attendees = models.ManyToManyField(Attendees)

    def __str__(self):
        return self.title
