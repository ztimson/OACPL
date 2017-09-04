import json

from django.shortcuts import render, HttpResponse

from .models import Newsletter, Subscriber


def newsletters(request):
    newsletters = Newsletter.objects.filter(sent=True).order_by('-publish')
    return render(request, 'newsletters.html', {'newsletters': newsletters})


def subscribe(request):
    try:
        Subscriber.objects.create(email=request.POST.get('email'))
        return HttpResponse(json.dumps({'success': True}), content_type='json')
    except Exception:
        return HttpResponse(json.dumps({'success': False}), content_type='json')
