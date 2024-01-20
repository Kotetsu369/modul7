import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://mfd.ru/currency/?currency=USD&from='
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 ''Firefox/50.0'})

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table', {'class': "mfd-table mfd-currency-table"})


table1 = [itog.text for itog in table]

table_list = table1[0].split()

day = []
rate = []

i = 4
while i< len(table_list):
    day.append(table_list[i])
    i = i+4
day_from_end = day.reverse()

t = 5
while t< len(table_list):
    rate.append(table_list[t])
    t = t+4
rate_from_end = rate.reverse()

rate=list(map(float,rate))
#print(rate)

import numpy as np
import matplotlib.pyplot as plt

#rate.remove('*')

plt.plot(day, rate, label='dollar')
plt.title('Dollart rate by days', fontsize=15)
plt.xlabel('Day', fontsize=12, color='blue')
plt.ylabel('dollar', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()

from matplotlib.pyplot import  MaxNLocator

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.grid(True)
ax.plot(day, rate)
plt.show()