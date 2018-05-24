from django.conf import settings
from django.contrib.auth.admin import User
from django.db import models
from django.utils import timezone

from tinymce import HTMLField


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attorney(models.Model):
    address = models.CharField(max_length=255)
    biography = HTMLField(blank=True, null=True)
    call_to_bar = models.CharField(max_length=4, blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True, on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    front_page = models.BooleanField(default=False)
    image = models.ImageField(upload_to='portraits', default='portraits/silhouette.png')
    joined = models.DateField(default=timezone.now)
    last_name = models.CharField(max_length=100)
    lso = models.CharField(max_length=20, blank= True, null=True)
    order = models.IntegerField(blank=True, null=True, verbose_name='Order On Front Page')
    phone = models.CharField(max_length=10)
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.DO_NOTHING)
    website = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

    def phone_formatted(self):
        if self.phone is None or self.phone == '': return ''
        return '({}) {}-{}'.format(self.phone[:3], self.phone[3:6], self.phone[6:])
    phone_formatted.short_description = 'Phone'

    def thumbnail(self):
        return '<img src="{}{}" height="50"/>'.format(settings.MEDIA_URL, str(self.image))
    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True

    def image_preview(self):
        return '<img src="{}{}"/>'.format(settings.MEDIA_URL, str(self.image))
    image_preview.short_description = 'Image'
    image_preview.allow_tags = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name
