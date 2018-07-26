from rest_framework import serializers
from .models import ExchangeRate


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'
