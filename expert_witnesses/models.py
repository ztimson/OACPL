from django.core.exceptions import ValidationError
from django.db import models

from case_law.models import Case


class AreaOfExpertise(models.Model):
    class Meta:
        verbose_name = 'Area of Expertise'
        verbose_name_plural = 'Areas of Expertise'

    field = models.CharField(max_length=255)

    def __str__(self):
        return self.field


class Expert(models.Model):

    class Meta(object):
        permissions = (
            ('view_cv', 'Can view CV'),
        )

    def validate_file_extension(value):
        if not value.name.endswith('.pdf'):
            raise ValidationError(u'File is not a PDF')

    cases = models.ManyToManyField(Case, blank=True)
    CV = models.FileField('CV', upload_to='cv', validators=[validate_file_extension], blank=True, null=True)
    expertise = models.ManyToManyField(AreaOfExpertise)
    institute = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
