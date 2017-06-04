from django import forms
from .models import Currency

class CurrencyConversionForm(forms.Form):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super(CurrencyConversionForm, self).__init__(*args, **kwargs)
        # if 'floating_currency' in self.data and 'base_currency' in self.data:
            # import ipdb; ipdb.set_trace()
            # self.fields['floating_currency'].queryset =  Currency.objects.all().filter(id=self.data['floating_currency'])
            # self.fields['base_currency'].queryset = Currency.objects.all().filter(id=self.data['base_currency'])


    base_currency_amount = forms.FloatField(required=False)
    base_currency = forms.ModelChoiceField(queryset=Currency.objects.all(),required=False)
    floating_currency = forms.ModelChoiceField(queryset=Currency.objects.all(),required=False)
    result_amount = forms.CharField(required=False)
