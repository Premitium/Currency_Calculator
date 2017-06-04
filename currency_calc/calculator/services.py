import requests
from .models import Currency
from bs4 import BeautifulSoup as bs
from re import sub
from decimal import Decimal

"""
Scraping data from an html table and
creating instances of the Currency model
"""
def createCurrencyInstances():
    xml_result = requests.get("http://www.bnb.bg/statistics/stexternalsector/stexchangerates/sterforeigncurrencies/index.htm")
    soup = bs(xml_result.content)
    rows = soup.find("table").find("tbody").find_all("tr")
    #Dumping the database table before every data load to avoid duplication
    Currency.objects.delete_everything()
    for row in rows:
        cells = row.find_all("td")
        #find last row in the table
        if cells[1]['class'][0] != 'last':
            currency_name = cells[0].get_text()
            currency_sign = cells[1].get_text()
            radix = int(cells[2].get_text())
            currency_to_bgn = calculateExchangeRateForOne(radix, cells[3].get_text())
            if cells[4].get_text():
                bgn_to_currency = Decimal(cells[4].get_text())
            else:
                bgn_to_currency = Decimal(-1)
            Currency.objects.create(currency_name=currency_name, currency_sign=currency_sign, currency_to_bgn=currency_to_bgn, bgn_to_currency=bgn_to_currency)

    return None

"""
The method equalizes all currency exchange radixes,
since some currency rates are given e.g 100 to 1
"""
def calculateExchangeRateForOne(radix, currency_to_bgn):
    value = Decimal(currency_to_bgn) / radix
    return value

"""
Calculate exchange rates according to a related currency.
In this case BGN.
"""
def calculateExchchangeRate(data):
    quantity = int(data.get('base_currency_amount'))

    base_currency_id = data.get('base_currency')
    float_currency_id = data.get('floating_currency')

    base_currency = Currency.objects.get_currency_sign_and_bgn_to_value(base_currency_id)
    float_currency = Currency.objects.get_currency_sign_and_bgn_to_value(float_currency_id)

    left_to_base_value = base_currency[1]
    right_to_base_value = float_currency[1]

    result = right_to_base_value * quantity / left_to_base_value

    return result
