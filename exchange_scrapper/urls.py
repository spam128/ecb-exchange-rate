from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.save_exchange),
    path('<name>/', views.ExchangeL.as_view()),
]
