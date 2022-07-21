from django.db import models
from django.forms import CharField


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    medium_price = models.DecimalField(max_digits=10, decimal_places=2) 
    large_price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.name
