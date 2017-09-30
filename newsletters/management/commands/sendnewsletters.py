from django.db.models import Q
from django.core import mail
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.html import strip_tags
from django.template.loader import render_to_string

from OACPL import settings
from newsletters.models import Newsletter, Subscriber


class Command(BaseCommand):
    help = 'Send out newsletter emails to subscribers'

    def handle(self, *args, **options):
        newsletters = Newsletter.objects.filter(Q(sent=False) & Q(publish__lte=timezone.now()))
        subscribers = Subscriber.objects.all().values_list('email', flat=True)
        print('Found %s unsent newsletters' % len(newsletters))
        print('Found %s subscribers' % len(subscribers))
        for newsletter in newsletters:
            print('Sending newsletter: "%s"' % newsletter.subject)
            mail.send_mail(newsletter.subject, strip_tags(newsletter.body), settings.EMAIL_HOST_USER, subscribers, html_message=render_to_string('email.html', {'content': newsletter.body}))
            newsletter.sent = True
            newsletter.save()
        print('Complete!')
