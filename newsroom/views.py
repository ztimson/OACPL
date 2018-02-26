from django.shortcuts import render

from .models import PressRelease


def newsroom(request):
    press_releases = PressRelease.objects.all()

    return render(request, 'newsroom.html', {'pressRelease': press_releases})
