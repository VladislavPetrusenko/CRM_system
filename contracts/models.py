from django.db import models
from services.models import Service


class Contract(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="contracts",
                                verbose_name="Услуга")
    file = models.FileField(upload_to="contracts/", verbose_name="Файл с документом")
    conclusion_date = models.DateField(verbose_name="Дата заключения")
    end_date = models.DateField(verbose_name="Дата окончания действия")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма")


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
        