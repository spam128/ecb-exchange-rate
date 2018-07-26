from django.test import TestCase
from unittest.mock import patch, MagicMock
from .models import ExchangeRate, ExchangeRSS

raw_html = '<ul class="zebraList"><li><a class="rss" href="/rss/fxref-usd.html">US dollar (USD)</a></li>'

class ExchangeRateTest(TestCase):



    @patch('exchange_scrapper.views.feedparser.parse')
    def test_save_exchange_rate(self, mock_feedparse):
        feeds = MagicMock()
        feeds['entries'][0]['cb_exchangerate'] = '1.1690 EUR'
        mock_feedparse.side_effect = lambda x: feeds
        resp = self.client.post('/exchange/create/', {'exchange': 'USD'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, '1.1690')

