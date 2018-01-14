from django.core.exceptions import ValidationError
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

    def validate_file_extension(value):
        if not value.name.endswith('.pdf'):
            raise ValidationError(u'File is not a PDF')

    published = models.DateField()
    headings = models.ManyToManyField(Heading)
    pdf = models.FileField('PDF', upload_to='case_law', validators=[validate_file_extension])
    synopsis = models.TextField()

    def __str__(self):
        return self.synopsis
