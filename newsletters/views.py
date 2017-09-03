from django.shortcuts import render

from .models import Newsletter


def newsletters(request):
    newsletters = Newsletter.objects.all()
    return render(request, 'newsletters.html', {'newsletters': newsletters})
