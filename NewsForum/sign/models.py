from django.db import models


class OneTimeCode(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    code = models.CharField(max_length=6)
    create_date = models.DateField(auto_now_add=True)
    expire_time = models.DateTimeField()

    def check_viability(self):
        pass
