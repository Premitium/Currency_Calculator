from django.shortcuts import render
# from .models import Currency
from .forms import CurrencyConversionForm
from .services import createCurrencyInstances, calculateExchchangeRate
import json
from django.http import HttpResponse



# Create your views here.
def index(request):
    # createCurrencyInstances()
    form = CurrencyConversionForm()

    if request.method == 'POST':
        form = CurrencyConversionForm(data=request.POST)
        if form.is_valid():
            result = calculateExchchangeRate(data=request.POST)
            if request.is_ajax():
                 return HttpResponse(result)

    return render(request, 'calculator/index.html', locals())
