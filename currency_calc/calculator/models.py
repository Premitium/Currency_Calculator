import moneyed
from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

class Currency(models.Model):
    from_currency = MoneyField(max_digits=10, decimal_places=2,default_currency='USD')
    to_curency = MoneyField(max_digits=10, decimal_places=2,default_currency='USD')
    name = models.TextField()
