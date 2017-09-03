from django.shortcuts import render

from .models import Attorney


def index(request, id):
    attorney = Attorney.objects.get(id=id)
    return render(request, 'attorney.html', {'attorney': attorney})
