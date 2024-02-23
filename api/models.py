from django.db import models
from django.contrib.auth.models import User, UserManager
# Create your models here.
from django import forms


class Product(models.Model):
    name = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(null=False, blank=False)
    password = forms.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.email
