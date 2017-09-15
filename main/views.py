from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.core import mail

from charter_members.models import Attorney
from newsletters.models import Subscriber
from OACPL import settings


def index(request):
    attorneys = Attorney.objects.filter(front_page=True)
    return render(request, 'index.html', {'attorneys': attorneys})


def login(request):
    if request.method == 'POST':
        if request.POST.get('request') == 'login':
            user = auth.authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'navbar': False, 'footer': False, 'failed': True})
        elif request.POST.get('request') == 'register':
            user = User.objects.create_user(request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'))
            user.save()
            if settings.EMAIL_HOST:
                mail.send_mail('OACPL Registration', 'You have successfully registered to the Ontario Asscocaition of Child Protection Lawyers!', settings.EMAIL_HOST_USER, [request.POST.get('email')])
            if request.POST.get('newsletter'):
                Subscriber.objects.create(email=request.POST.get('email'))
            # TODO: If Case law access was requested, send an email out to staff
            auth.login(request, user)
            return redirect('/')

        elif request.POST.get('request') == 'reset':
            # TODO: Reset password and send email
            pass
    else:
        return render(request, 'login.html', {'navbar': False, 'footer': False})


def logout(request):
    auth.logout(request)
    return redirect('/')
