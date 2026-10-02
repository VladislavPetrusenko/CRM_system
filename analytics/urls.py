"""Маршруты приложения статистики"""

from django.urls import path
from .views import CompaignStatisticView

urlpatterns = [
    path('', CompaignStatisticView.as_view(), name='compaign_analytics')
]
