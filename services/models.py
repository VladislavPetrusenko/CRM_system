from django.db import models
from django.urls import reverse


class Service(models.Model):
    """Предоставляемая услуга."""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


    def get_absolute_url(self):
        """URL детальной страницы услуги."""
        return reverse("service_detail", kwargs={"pk": self.pk})
    