"""Админка для лидов"""

from django.contrib import admin
from leads.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Поля админки"""
    list_display = ('full_name', 'phone', 'email', 'compaign')
    list_filter = ('compaign',)
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)
