from django.urls import path
from .views import CurrencyConvertView

urlpatterns = [
    path('convert/', CurrencyConvertView.as_view(), name='currency_convert'),
]
