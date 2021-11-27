from django.db import models


class Section(models.Model):
    class Meta:
        db_table = "section"
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    name = models.CharField(max_length=255, verbose_name="Наименование раздела")
    description = models.CharField(max_length=255, verbose_name="Описание")

    def __str__(self):
        return f"{self.description}"
