import mimetypes

from django.db.models import Q
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from django.utils import timezone

from OACPL import settings
from OACPL.utils import url_fix_render_to_string
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
            msg = EmailMessage(subject=newsletter.subject, body=url_fix_render_to_string('email.html', {'content': newsletter.body, 'unsubscribe': True}), from_email=settings.EMAIL_HOST_USER, bcc=subscribers)
            msg.content_subtype = 'html'
            for attachment in newsletter.attachments.all():
                msg.attach(attachment.name(), attachment.file.read(), mimetypes.guess_type(attachment.name())[0])
            msg.send()
            newsletter.sent = True
            newsletter.save()
        print('Complete!')
