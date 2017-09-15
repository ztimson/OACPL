import json

from django.shortcuts import HttpResponse, render, redirect
from django.contrib import auth

from charter_members.models import Attorney


def index(request):
    attorneys = Attorney.objects.filter(front_page=True)
    return render(request, 'index.html', {'attorneys': attorneys})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request)
        if user:
            return HttpResponse(json.dumps({'status': True}))
        else:
            return HttpResponse(json.dumps({'status': False}))
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
