import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
import feedparser
from .models import ExchangeRate
from django.utils.dateparse import parse_datetime

url = 'https://www.ecb.europa.eu/home/html/rss.en.html'
exchanges_list_class = 'zebraList'


def exchange(request, exchange_name):
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    html.find_all('ul', {'class': exchanges_list_class})

    feeds = feedparser.parse('https://www.ecb.europa.eu/rss/fxref-usd.html')
    exchange_rate = float(feeds['entries'][0]['cb_exchangerate'].split()[0])
    ExchangeRate.objects.create(value=exchange_rate, date=parse_datetime(feeds['entries'][0]['updated']))
    return HttpResponse()
