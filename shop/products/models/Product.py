from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

from .Section import Section


class Product(models.Model):
    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    units = (("items", "Штук"),)

    name = models.CharField(max_length=64, verbose_name="Наименование")
    date_of_receipt = models.DateField(verbose_name="Дата поставки")
    price = models.PositiveIntegerField(verbose_name="Цена")
    unit = models.CharField(max_length=10, choices=units, verbose_name="еденица измерения")
    provider_name = models.CharField(max_length=64, verbose_name="Наименование поставщика")
    section = models.ManyToManyField(Section, verbose_name="Разделы", related_name='section')

    site = models.ManyToManyField(Site, null=True)

    def __str__(self):
        return f"{self.name}"

    def get_units(self):
        return dict(self.units)[self.unit]
