import json

from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone

from .models import Newsletter, Subscriber


def newsletters(request):
    if request.method == 'POST':
        Subscriber.objects.create(email=request.POST.get('email'))
    newsletters = Newsletter.objects.filter(Q(publish__lte=timezone.now())).order_by('-publish')
    return render(request, 'newsletters.html', {'newsletters': newsletters})
