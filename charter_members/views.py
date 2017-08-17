from django.shortcuts import render

from .models import Attorney


def index(request, userId):
    attorney = Attorney.objects.get(id=userId)
    return render(request, 'attorney.html', {'attorney': attorney})
