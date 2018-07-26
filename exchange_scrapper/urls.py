from django.urls import path
from . import views

urlpatterns = [
    path('create/<exchange_name>/', views.save_exchange),
    path('', views.ExchangeLC.as_view()),
]
