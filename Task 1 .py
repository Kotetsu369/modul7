import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://mfd.ru/currency/?currency=USD&from='
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 ''Firefox/50.0'})

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table', {'class': "mfd-table mfd-currency-table"})

table1 = [itog.text for itog in table]

string = ''
for el in table1:
    string += str(el) #Превращаем каждый элемент списка в строку
string.replace('\n', '')


print(string)
#print([itog.text for itog in table1])



