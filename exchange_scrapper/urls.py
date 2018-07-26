from django.urls import path
from . import views

urlpatterns = [
    path('<exchange_name>/', views.exchange)
]
