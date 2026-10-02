"""Конфиг для приложения клиенты"""

from django.apps import AppConfig


class ClientsConfig(AppConfig):
    """Класс конфига"""
    name = 'clients'
    verbose_name = 'Активные клиенты'
