from django.shortcuts import render, redirect
from django.contrib import auth

from charter_members.models import Attorney


def index(request):
    attorneys = Attorney.objects.filter(front_page=True)
    return render(request, 'index.html', {'attorneys': attorneys})


def logout(request):
    auth.logout(request)
    return redirect('/')
