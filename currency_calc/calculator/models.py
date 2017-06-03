from django.db import models
from .managers import CurrencyManager

class Currency(models.Model):
    currency_name = models.TextField(max_length=225)
    currency_sign = models.CharField(max_length=3)
    currency_to_bgn = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bgn_to_currency = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    objects = CurrencyManager()

    def __str__(self):
        return self.currency_name
