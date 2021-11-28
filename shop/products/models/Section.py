from django.db import models
from django.contrib.sites.models import Site


class Section(models.Model):
    class Meta:
        db_table = "section"
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    name = models.CharField(max_length=255, verbose_name="Наименование раздела")
    description = models.CharField(max_length=255, verbose_name="Описание")

    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.description}"
