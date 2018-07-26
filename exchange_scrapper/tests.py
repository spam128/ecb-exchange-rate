from django.test import TestCase
from unittest.mock import patch, Mock
from .models import ExchangeRate

raw_html = '<ul class="zebraList"><li><a class="rss" href="/rss/fxref-usd.html">US dollar (USD)</a></li>'


class ExchangeRateTest(TestCase):

    @patch('exchange_scrapper.views.requests.get')
    def test_get_exchange_rate(self, mock_get):
        mock_html = Mock()
        mock_html.text = raw_html
        mock_get.return_value = mock_html
        resp = self.client.get('/exchange/usd/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ExchangeRate.objects.count(), 1)
