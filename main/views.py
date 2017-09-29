from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User, Permission
from django.core import mail
from django.db.models import Q
from django.shortcuts import render, redirect

from charter_members.models import Attorney
from newsletters.models import Subscriber
from OACPL import settings


def index(request):
    attorneys = Attorney.objects.filter(front_page=True)
    return render(request, 'index.html', {'attorneys': attorneys})


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    body = request.POST.get('body')

    result = False
    if name is not None and email is not None and subject is not None and body is not None:
        result = mail.send_mail('OACPL CONTACT: %(subject)s' % locals(), body, settings.EMAIL_HOST_USER, [settings.EMAIL_CONTACT],
                                html_message='<strong>From:</strong> %(name)s (%(email)s)<br><br>{body}' % locals())

    return JsonResponse({'success': True if result else False})


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
            user = User.objects.create_user(request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
            user.save()
            if settings.EMAIL_HOST:
                mail.send_mail('OACPL Registration', 'You have successfully registered to the Ontario Association of Child Protection Lawyers!', settings.EMAIL_HOST_USER, [request.POST.get('email')])
            if request.POST.get('newsletter'):
                Subscriber.objects.create(email=request.POST.get('email'))
            if request.POST.get('caselaw'):
                perm = Permission.objects.get(codename='change_user')
                admins = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm) | Q(is_superuser=True)).distinct().values_list('email', flat=True)
                print(admins)
                mail.send_mail('OACPL Case Law Request', '%(user.email)s has requested case law access.', settings.EMAIL_HOST_USER, admins, html_message='<a href="#">%(user.email)s</a> has requested case law access.')
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html', {'navbar': False, 'footer': False})


def logout(request):
    auth.logout(request)
    return redirect('/')
