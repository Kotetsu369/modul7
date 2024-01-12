import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://mfd.ru/currency/?currency=USD&from='
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 ''Firefox/50.0'})

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.findAll('table', {'class': "mfd-table mfd-currency-table"})

print([itog.text for itog in table])



