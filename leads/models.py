"""Модели БД"""

from django.db import models
from django.urls import reverse
from compaigns.models import Compaign


class Lead(models.Model):
    """Поля модели"""
    full_name = models.CharField(max_length=200, verbose_name="Ф. И. О.")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    compaign = models.ForeignKey(Compaign, on_delete=models.CASCADE, related_name="leads",
                                 verbose_name="Рекламная кампания")


    def __str__(self):
        """Строковое представление"""
        return self.full_name


    class Meta:
        """Настройки модели"""
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"


    def get_absolute_url(self):
        """URL детальной страницы потенциального клиента."""
        return reverse("lead_detail", kwargs={"pk": self.pk})
