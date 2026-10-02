"""
Админка для контрактов
"""

from django.contrib import admin
from django.utils.html import format_html

from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """Отображение админки"""
    list_display = ('name', 'service', 'conclusion_date', 'end_date', 'amount', 'file_link')
    list_filter = ('service',)
    search_fields = ('name',)
    date_hierarchy = 'conclusion_date'


    @admin.display(description='Документ')
    def file_link(self, obj):
        """Отображение кнопки для скачивания файла"""
        if obj.file:
            return format_html('<a href="{}">Скачать</a>', obj.file.url)
        return '--'
