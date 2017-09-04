from django.conf import settings
from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=50)

    def __str__(self):
        return self.position_name


class Attorney(models.Model):
    biography = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    front_page = models.BooleanField(default=False)
    image = models.ImageField(upload_to='portraits', default='portraits/silhouette.png')
    joined = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, blank=True, null=True)
    position = models.ForeignKey(Position)
    website = models.CharField(max_length=255, blank=True, null=True)

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
        return self.name
