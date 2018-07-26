from django.db import models


class ExchangeRate(models.Model):
    value = models.FloatField()
    date = models.DateTimeField()
