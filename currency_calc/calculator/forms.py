from django import forms

from .models import Currency

class CurrencyConversionForm(forms.Form):
    class Meta:
        model = Currency
        fields = ('from_currency', 'to_curency', 'name')
