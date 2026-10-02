"""Админка сервисов"""

from django.contrib import admin
from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Поля админки"""
    list_display = ('name', 'price')
    search_fields = ('name',)
    ordering = ('name',)
