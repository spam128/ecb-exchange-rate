import feedparser
from .models import ExchangeRate, ExchangeRSS
from django.utils.dateparse import parse_datetime
from rest_framework import generics
from .serializers import ExchangeSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

main_url = 'https://www.ecb.europa.eu/'


@csrf_exempt
def save_exchange(request):
    exchange_name = request.POST['name']
    slug = get_object_or_404(ExchangeRSS, name=exchange_name).slug
    feeds = feedparser.parse(main_url + slug)
    exchange_rate = float(feeds['entries'][0]['cb_exchangerate'].split()[0])
    exchange = ExchangeRate.objects.get_or_create(value=exchange_rate,
                                                  date=parse_datetime(feeds['entries'][0]['updated']),
                                                  name=exchange_name)
    return render(request, 'exchange_scrapper/object_created.html', {'exchange': exchange[0], 'created': exchange[1]})


class ExchangeL(generics.ListAPIView):
    serializer_class = ExchangeSerializer

    def get_queryset(self):
        return ExchangeRate.objects.filter(name=self.kwargs['name']).order_by('-date')
