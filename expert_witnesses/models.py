from django.db import models

from case_law.models import Case


class AreaOfExpertise(models.Model):
    class Meta:
        verbose_name = 'Area of Expertise'
        verbose_name_plural = 'Area of Expertise'

    field = models.CharField(max_length=255)

    def __str__(self):
        return self.field


class Expert(models.Model):
    cases = models.ManyToManyField(Case, null=True, blank=True)
    expertise = models.ManyToManyField(AreaOfExpertise)
    institute = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
