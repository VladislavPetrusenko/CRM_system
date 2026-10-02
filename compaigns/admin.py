"""Админка для клиентов"""

from django.contrib import admin
from compaigns.models import Compaign
from leads.models import Lead


class LeadInline(admin.TabularInline):
    """Инлайны в админке"""
    model = Lead
    extra = 0


@admin.register(Compaign)
class CompaignAdmin(admin.ModelAdmin):
    """Регистрация полей в админке"""
    list_display = ('name', 'service', 'channel_display', 'budget', 'leads_count')
    list_filter = ('channel', 'service')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = (LeadInline,)


    @admin.display(description='Канал продвижения')
    def channel_display(self, obj):
        """Отображение канала продвижения"""
        return obj.get_channel_display()


    @admin.display(description='Число лидов')
    def leads_count(self, obj):
        """Отображает число лидов"""
        return obj.leads.count()
