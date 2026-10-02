"""Модели БД клиентов"""

from django.db import models
from django.urls import reverse
from leads.models import Lead
from contracts.models import Contract


class ActiveClient(models.Model):
    """Поля модели"""
    lead = models.OneToOneField(
        Lead,
        on_delete=models.CASCADE,
        related_name="active_client",
        verbose_name="Потенциальный клиент"
    )
    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name="active_client",
        verbose_name="Контракт"
    )


    def __str__(self):
        """Строковое представление вывода"""
        return self.lead.full_name


    class Meta:
        """Настройки модели"""
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"


    def get_absolute_url(self):
        """URL детальной страницы активного клиента."""
        return reverse('client_detail', kwargs={'pk': self.pk})
