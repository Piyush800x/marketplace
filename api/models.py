from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
