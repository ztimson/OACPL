from django.shortcuts import render

from .models import Newsletter


def newsletters(request):
    newsletters = Newsletter.objects.filter(sent=True).order_by('-publish')
    return render(request, 'newsletters.html', {'newsletters': newsletters})
