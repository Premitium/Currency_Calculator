from django.shortcuts import render
from .models import Currency
from .forms import CurrencyConversionForm
from .services import createCurrencyInstances

# Create your views here.
def index(request):
    createCurrencyInstances()

    return render(request, 'calculator/index.html', locals())
