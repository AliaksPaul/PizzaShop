from django.db import models
from django.conf import settings

# Create your models here.


class Adress(models.Model):
    customer = models.CharField()
    postal_code = models.BigIntegerField(null=False)
    address_name = models.CharField()
    address_line1 = models.CharField()
    address_line2 = models.CharField()
    city = models.CharField()
    landmark = models.CharField()
    is_deleted = models.BooleanField(default=False)

