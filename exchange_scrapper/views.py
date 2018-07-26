import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
import feedparser
from .models import ExchangeRate, ExchangeRSS
from django.utils.dateparse import parse_datetime
from rest_framework import generics
from .serializers import ExchangeRate
from django.shortcuts import get_object_or_404
from django.shortcuts import render

main_url = 'https://www.ecb.europa.eu/'


def save_exchange(request, exchange_name):
    slug = get_object_or_404(ExchangeRSS, name=exchange_name).slug
    feeds = feedparser.parse(main_url + slug)
    exchange_rate = float(feeds['entries'][0]['cb_exchangerate'].split()[0])
    exchange = ExchangeRate.objects.get_or_create(value=exchange_rate,
                                                  date=parse_datetime(feeds['entries'][0]['updated']),
                                                  name=exchange_name)

    return render(request, 'exchange_scrapper/object_created.html', {'exchange': exchange[0], 'created': exchange[1]})


class ExchangeLC(generics.ListCreateAPIView):
    queryset = ExchangeRate.objects.all().order_by('-date')
    serializer_class = ExchangeRate
