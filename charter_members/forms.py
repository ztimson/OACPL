from django.core import mail
from django import forms
from django.contrib.auth.models import Group, User

from newsletters.models import Subscriber
from .models import Attorney, Position
from OACPL import settings
from OACPL.utils import render_to_string


class RegisterForm(forms.ModelForm):
    def email_validator(self):
        if User.objects.filter(email=self).exists():
            raise forms.ValidationError('This email is already registered')

    def password_length(self):
        if len(self) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long')

    biography = forms.CharField(widget=forms.Textarea, required=False, label='Biography')
    call_to_bar = forms.CharField(max_length=4, required=False, label='Year of Call to Bar')
    case_law = forms.BooleanField(initial=True, required=False)
    email = forms.EmailField(max_length=255, validators=[email_validator])
    lso = forms.CharField(max_length=20, required=False, label='LSO #')
    newsletter = forms.BooleanField(initial=True, required=False)
    request_training = forms.CharField(max_length=255, required=False, label='Request Training For...')
    password1 = forms.CharField(widget=forms.PasswordInput(), validators=[password_length])
    password2 = forms.CharField(widget=forms.PasswordInput())
    provide_training = forms.CharField(max_length=255, required=False, label='Offer Training For...')
    tos = forms.BooleanField(initial=False, required=True)

    class Meta:
        model = Attorney
        fields = ['first_name', 'last_name', 'region', 'password1', 'password2', 'image', 'email', 'address', 'phone', 'website', 'call_to_bar', 'lso', 'biography', 'provide_training', 'request_training', 'case_law', 'newsletter', 'tos']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        password_confirm = cleaned_data.get('password2')
        if password != password_confirm:
            raise forms.ValidationError("The two password fields must match.")
        return cleaned_data

    def save(self, commit=True):
        # Create attorney profile
        user = super().save(commit=False)
        member = Position.objects.filter(name='Member').first()
        if member:
            user.position = member
        user.save()

        # Send confirmation email
        mail.send_mail('OACPL Registration', 'You have successfully registered to the Ontario Association of Child Protection Lawyers!', settings.EMAIL_HOST_USER, [user.email], html_message=render_to_string('email.html', {'content': 'You have successfully registered to the Ontario Association of Child Protection Lawyers!', 'name': user.first_name + ' ' + user.last_name, 'base_url': settings.BASE_URL}))

        # Subscribe to newsletters
        if self.cleaned_data['newsletter'] == 'on' and not Subscriber.objects.filter(email=user.email).exists():
            Subscriber.objects.create(email=user.email)

        # Send email to register@oacpl.org
        body = '{} {} ({}) has registered with OACPL. <br><br>'.format(user.first_name, user.last_name, user.email)
        if self.cleaned_data['case_law'] == 'on':
            body += 'They have request access to case law. <br><br>'
        if self.cleaned_data['provide_training']:
            body += 'They have offered to provide training for: {}. <br><br>'.format(self.cleaned_data['provide_training'])
        if self.cleaned_data['request_training']:
            body += 'They have request training for: {}. <br><br>'.format(self.cleaned_data['request_training'])
        mail.send_mail(user.first_name + ' ' + user.last_name, body.replace('<br>', ' '), settings.EMAIL_HOST_USER, ['register@oacpl.org'], html_message=render_to_string('email.html', {'content': body, 'base_url': settings.BASE_URL}))

        # Create Auth
        auth = User.objects.create_user(user.email, first_name=user.first_name, last_name=user.last_name, email=user.email, password=self.cleaned_data['password1'])
        auth.save()

        # Add user to default Group
        default_group = Group.objects.filter(name='default').first()
        if default_group:
            default_group.user_set.add(auth)

        return auth
