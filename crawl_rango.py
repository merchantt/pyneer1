import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango.settings')

import django
django.setup()
from rango.models import Notice
from django.core.exceptions import ObjectDoesNotExist

import requests
from bs4 import BeautifulSoup
import datetime


def crawler():

    page = 1
    increase_page = True
    while increase_page and page < 2:

        notice_list = []

        ## Webpage parsing ##
        url = 'http://www.skku.edu/new_home/campus/skk_comm/notice_list.jsp?page=' + '%d' % (page) \
              + '&bCode=0'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        table_td = soup.tbody.find_all('td')

        ## Get parsing_lists ##

        Number = []
        Date = [str(datetime.date.today())] * 10
        Time = []
        Title = []
        Unread = [1]*10


        for i in range(0,50):
            if i % 5 == 0:
                Number.append(int(table_td[i].string))
            if i % 5 == 1:
                Title.append(str(table_td[i].string))
            if i % 5 == 2:
                Time.append(str(table_td[i].string))

        for i in range(10):
            if len(Time[i]) == len(Date[i]):
                Date[i] = Time[i]

        for i in range(10):
            info = {}
            info["Number"] = Number[i]
            info["Title"] = Title[i]
            info["Date"] = Date[i]
            info["Unread"] = Unread[i]

            notice_list.append(info)

        page += 1
        for i in notice_list:
            add_notice(i["Title"],i["Number"],i["Date"],i["Unread"])

def add_notice(title, num, date, unread):
    try:
        Notice.objects.get(title=title)
    except Notice.DoesNotExist:
        n = Notice.objects.get_or_create(title=title)[0]
        n.num = num
        n.date = date
        n.unread = unread
        n.save()
        return n

if __name__ == '__main__':
    print("Starting notice refresh ...")
    crawler()