from django.shortcuts import render
from .models import Currency
from .forms import CurrencyConversionForm
from .services import getXML


# Create your views here.
def index(request):
    resultXMLList = getXML()
    import ipdb; ipdb.set_trace()
    form = CurrencyConversionForm()
    if request.method == 'POST':
        form = form(data=request.POST)
    else:
        form = form # this is important

    return render(request, 'calculator/index.html', locals())
