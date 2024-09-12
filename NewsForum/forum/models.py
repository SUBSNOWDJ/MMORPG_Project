from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name.title()


class Ticket(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('guildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('leatherworkers', 'Кожевники'),
        ('potionmakers', 'Зельевары'),
        ('spellcasters', 'Мастера заклинаний'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='tanks',
        verbose_name='Категория'
    )
    head = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')
    pubdate = models.DateField(auto_now_add=True)

    def close_ticket(self):
        self.status = False
        self.save()


class TicketCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ticket}: {self.category}'


class Responds(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)


class News(models.Model):
    head = models.CharField(max_length=255)
    text = models.TextField()
