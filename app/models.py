from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=30, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=40, unique=True)

    def __str__(self):
        return self.username


class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code


class Account(models.Model):
    name = models.CharField(max_length=30)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.currency.code
