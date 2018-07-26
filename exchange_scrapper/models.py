from django.db import models


class ExchangeRate(models.Model):
    value = models.FloatField()
    date = models.DateTimeField()
    name = models.CharField(max_length=5)


class ExchangeRSS(models.Model):
    name = models.CharField(max_length=5, unique=True)
    slug = models.SlugField(max_length=40)
