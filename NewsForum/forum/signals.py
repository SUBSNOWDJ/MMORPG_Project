from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Responds


@receiver(post_save, sender=Responds)
def notify_about_respond(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'New respond to your ticket',
            message=f'New respond to your ticket: {instance.ticket.head}',
            from_email='user@yandex.ru',
            recipient_list=[instance.ticket.author.email],
            fail_silently=False
        )
