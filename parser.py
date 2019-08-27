#!/home/qwil/Localparser/venv/bin/python


import requests
from bs4 import BeautifulSoup as bs
import time

headers = {'accept': '*/*',
                     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36'}
base_url = 'https://www.cbr.ru/'

def cbrf_pars(base_url, headers):
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('join')
        soup = bs(request.content, 'html.parser')
        div = soup.find_all('div', attrs={'id':'widget_exchange'})
        print(div)
        file = open('/home/qwil/Localparser/Currency Rates_{}.txt'.format(time.ctime()), "w")
        file.write(str(div))
        file.close()
    else:
        print('error 404 page not found')
cbrf_pars(base_url, headers)
