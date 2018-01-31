import random

from django.http import JsonResponse
from django.contrib import auth
from django.core import mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from OACPL.utils import render_to_string
from .models import ResetToken
from charter_members.forms import RegisterForm
from OACPL.utils import url_fix_render_to_string
from charter_members.models import Attorney
from OACPL import settings
from variables.models import Variable


def index(request):
    attorneys = Attorney.objects.filter(front_page=True).order_by('order')
    banner = Variable.objects.get(key='banner')
    popup_header = Variable.objects.get(key='popup_header')
    popup_body = Variable.objects.get(key='popup_body')
    objectives = Variable.objects.get(key='objectives')
    return render(request, 'index.html', {'attorneys': attorneys, 'contact': settings.EMAIL_CONTACT, 'youtube': settings.YOUTUBE_CONFERENCE, 'banner': banner, 'objectives': objectives, 'popup_header': popup_header, 'popup_body': popup_body})


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    body = request.POST.get('body')

    result = False
    if name is not None and email is not None and subject is not None and body is not None:
        result = mail.send_mail('OACPL CONTACT: %(subject)s' % locals(), body, settings.EMAIL_HOST_USER, [settings.EMAIL_CONTACT],
                                html_message=url_fix_render_to_string('email.html', {'content': '<strong>Someone has messaged you via the website contact form!<br><br>Subject:</strong> %(subject)s<br><strong>From:</strong> %(name)s <%(email)s><br><br>%(body)s' % locals(), 'signature': ' '}))

    return JsonResponse({'success': True if result else False})


def login(request):
    terms = Variable.objects.get(key='terms')
    if request.method == 'POST':
        if request.POST.get('request') == 'register':
            register_form = RegisterForm(request.POST, request.FILES)
            if register_form.is_valid():
                user = register_form.save()
                auth.login(request, user)
                return redirect('/')
        elif request.POST.get('request') == 'login':
            user = auth.authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'navbar': False, 'footer': False, 'failed': True})

    if 'register_form' not in vars():
        register_form = RegisterForm()
    return render(request, 'login.html', {'navbar': False, 'footer': False, 'register': register_form, 'terms': terms})


def reset(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            reset_req = ResetToken.objects.filter(token=request.POST.get('token')).first()
            reset_req.user.set_password(request.POST.get('password1'))
            reset_req.user.save()
            auth.login(request, reset_req.user)
            reset_req.delete()
            return redirect('/')

    return render(request, 'reset.html', {'navbar': False, 'footer': False, 'token': request.GET.get('token')})


def reset_token(request):
    user = User.objects.filter(email=request.POST.get('email')).first()
    if user:
        token = ''.join([chr(random.randrange(97, 122)) for i in range(8)])
        reset = ResetToken.objects.create(token=token, user=user)
        reset.save()
        mail.send_mail('OACPL Password Recovery', 'To reset your password navigate to https://oacpl.org/reset and enter code: ' + token, settings.EMAIL_HOST_USER, [user.email], html_message=render_to_string('email.html', {'content': 'To reset your password click <a href="/reset?token={}">here</a>.<br><br>If the link does not work, please navigate to {}/reset and enter the following code: {}'.format(token, settings.BASE_URL, token), 'name': user.first_name + ' ' + user.last_name, 'base_url': settings.BASE_URL}))
    return JsonResponse({'success': True})


def logout(request):
    auth.logout(request)
    return redirect('/')
