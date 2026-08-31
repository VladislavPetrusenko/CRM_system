from django.db import models
from services.models import Service


class Compaign(models.Model):
    CHANNELS = (
        ("social", "Социальные сети"),
        ("context", "Контекстная реклама"),
        ("targeting", "Таргетированная реклама"),
        ("email", "Email-рассылка"),
        ("other", "Другое"),
    )

    name = models.CharField(max_length=200, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="compaigns",
                                verbose_name="Рекламируемая услуга")
    channel = models.CharField(max_length=50, choices=CHANNELS, verbose_name="Канал продвижения")
    budget = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Бюджет на рекламу")


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"
        