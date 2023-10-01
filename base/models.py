from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(null=False, blank=False)
    img = models.TextField(null=False, blank=False)
    products = models.ForeignKey('Product', on_delete=models.CASCADE)
    address = models.CharField(
        max_length=500, blank=False, null=False, default='new york')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    desc = models.TextField(null=False, blank=False)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
