from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OneTimeCode


@receiver(post_save, sender=OneTimeCode)
def send_code(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=f'Conformation code',
            message=f'Your conformation code: {instance.code}',
            from_email='anastaciazybkina@yandex.ru',
            recipient_list=[instance.email],
            fail_silently=True
        )
