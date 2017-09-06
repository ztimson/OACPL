from django.db import models


class Heading(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Case(models.Model):

    class Meta(object):
        permissions = (
            ('view_pdf', 'Can view PDF'),
        )

    published = models.DateField()
    headings = models.ManyToManyField(Heading)
    pdf = models.FileField(upload_to='secure')
    synopsis = models.TextField()

    def __str__(self):
        return self.synopsis
