import requests
from bs4 import BeautifulSoup as bs

def getXML():
    xml_result = requests.get("http://www.bnb.bg/statistics/stexternalsector/stexchangerates/sterforeigncurrencies/index.htm")
    soup = bs(xml_result.content)

    rows = soup.find("table").find("tbody").find_all("tr")
    rawCurrencyData = []
    for row in rows:
        cells = row.find_all("td")
        #find last row in the table
        if cells[1]['class'][0] != 'last':
            currency_name = cells[0].get_text()
            currency_sign = cells[1].get_text()
            currency_to_bgn = cells[3].get_text()
            bgn_to_currency = cells[4].get_text()
            rawCurrencyData.append((currency_name,currency_sign,currency_to_bgn,bgn_to_currency))

    return rawCurrencyData
