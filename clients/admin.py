"""Админка приложения клиенты"""

from django.contrib import admin
from clients.models import ActiveClient


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    """Вид отображения админки"""
    list_display = ('lead', 'contract')
    search_fields = ('lead__full_name', 'contract__name')
