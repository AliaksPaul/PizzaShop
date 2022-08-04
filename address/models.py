from django.db import models
from django.conf import settings

# Create your models here.


class Adress(models.Model):
    customer = models.CharField(max_length=1000)
    postal_code = models.BigIntegerField(max_length=12, null=False)
    address_name = models.CharField(max_length=1000)
    address_line1 = models.CharField(max_length=1000)
    address_line2 = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    landmark = models.CharField(max_length=1000)
    is_deleted = models.BooleanField(default=False)

