
#!/home/qwil/Localparser/venv/bin/python

import requests
from bs4 import BeautifulSoup as bs, BeautifulSoup
import time


def find_table_rate():
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36'}
    base_url = 'https://www.cbr.ru/'
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('join')
        soup = bs(request.content, 'html.parser')
        divi = soup.find_all('div', attrs={'id':'widget_exchange'})
        return divi

def save_rates():
    # -*- coding: utf-8 -*-
    file = open('pars.txt', "w")
    file.write(str(find_table_rate()))
    file.close()
save_rates()

def format_html():
    # -*- coding: utf-8 -*-
    with open('pars.txt', 'r') as file:
        html = file.read()
    result = ''.join(BeautifulSoup(html).findAll(text=True))
    file = open('pars.txt', "w")
    file.write(str(result))
    file.close()
format_html()

def format_rate():
    # -*- coding: utf-8 -*-
    with open('pars.txt') as file:
        course = [row.strip() for row in file]
        dol= 'Курс доллара \n', course[18]
        evr = 'Курс евро \n', course[29]
        file = open('Currency Rates_{}.txt'.format(time.ctime()), "w")
        file.write(str(dol))
        file.write('\n')
        file.write(str(evr))
        file.close()
format_rate()
