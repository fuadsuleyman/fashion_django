import time
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
# from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Subscriber

@shared_task
def dump_database():
    print('database dump olunmaga basladi')
    time.sleep(30)
    print('database dump olundu')


@shared_task
def send_mail_to_subscribers():
    subscriber_emails = Subscriber.objects.values_list('email', flat=True)

    context = {
        'site_address': settings.SITE_ADDRESS,
    }

    html_message = render_to_string('index/email_template.html', context)
    subject = 'News About our site'

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=settings.EMAIL_HOST_USER,
        to=subscriber_emails,
        )
    email.content_subtype = 'html'
    email.send()