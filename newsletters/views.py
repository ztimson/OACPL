import json

from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.utils import timezone

from .models import Newsletter, Subscriber


def newsletters(request):
    newsletters = Newsletter.objects.filter(Q(publish__lte=timezone.now())).order_by('-publish')
    return render(request, 'newsletters.html', {'newsletters': newsletters})


def subscribe(request):
    try:
        Subscriber.objects.create(email=request.POST.get('email'))
        return HttpResponse(json.dumps({'success': True}), content_type='json')
    except Exception:
        return HttpResponse(json.dumps({'success': False}), content_type='json')
