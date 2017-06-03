import requests
from .models import Currency
from bs4 import BeautifulSoup as bs
from re import sub
from decimal import Decimal

def createCurrencyInstances():
    xml_result = requests.get("http://www.bnb.bg/statistics/stexternalsector/stexchangerates/sterforeigncurrencies/index.htm")
    soup = bs(xml_result.content)
    rows = soup.find("table").find("tbody").find_all("tr")
    Currency.objects.delete_everything()
    # rawCurrencyData = []
    for row in rows:
        cells = row.find_all("td")
        #find last row in the table
        if cells[1]['class'][0] != 'last':
            currency_name = cells[0].get_text()
            currency_sign = cells[1].get_text()
            radix = int(cells[2].get_text())
            currency_to_bgn = calculateExchangeRageForOne(radix, cells[3].get_text())
            if cells[4].get_text():
                bgn_to_currency = Decimal(cells[4].get_text())
            else:
                bgn_to_currency = Decimal(-1)
            # rawCurrencyData.append((currency_name,currency_sign,currency_to_bgn,bgn_to_currency))
            Currency.objects.create(currency_name=currency_name, currency_sign=currency_sign, currency_to_bgn=currency_to_bgn, bgn_to_currency=bgn_to_currency)

    return None

def calculateExchangeRageForOne(radix, currency_to_bgn):
    value = Decimal(currency_to_bgn) / radix
    return value
