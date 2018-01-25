from django.http import JsonResponse
from django.contrib import auth
from django.core import mail
from django.shortcuts import render, redirect

from charter_members.forms import RegisterForm
from OACPL.utils import url_fix_render_to_string
from charter_members.models import Attorney
from OACPL import settings


def index(request):
    attorneys = Attorney.objects.filter(front_page=True).order_by('order')
    return render(request, 'index.html', {'attorneys': attorneys, 'contact': settings.EMAIL_CONTACT, 'youtube': settings.YOUTUBE_CONFERENCE})


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
    return render(request, 'login.html', {'navbar': False, 'footer': False, 'register': register_form})


def logout(request):
    auth.logout(request)
    return redirect('/')
