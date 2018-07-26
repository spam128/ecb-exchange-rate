from django.test import TestCase
from unittest.mock import patch
from exchange_scrapper.models import ExchangeRate


class ExchangeRateTest(TestCase):

    @patch('exchange_scrapper.views.feedparser.parse')
    def test_save_exchange_rate(self, mock_feedparse):
        feeds = {'entries': [{'cb_exchangerate': '1.1690 EUR', 'updated': '2018-07-26T14:15:00+01:00'}]}
        mock_feedparse.return_value = feeds
        self.assertEqual(ExchangeRate.objects.count(), 0)
        resp = self.client.post('/exchange/create/', {'name': 'USD'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'exchange_scrapper/object_created.html')
        self.assertEqual(ExchangeRate.objects.count(), 1)
        exchange_rate = ExchangeRate.objects.first()
        self.assertEqual(exchange_rate.value, 1.169)
        self.assertEqual(exchange_rate.name, 'USD')
