from django.db import models
from leads.models import Lead
from contracts.models import Contract


class ActiveClient(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name="active_client",
                                verbose_name="Потенциальный клиент")
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="active_client",
                                    verbose_name="Контракт")


    def __str__(self):
        return self.lead.full_name


    class Meta:
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"
        