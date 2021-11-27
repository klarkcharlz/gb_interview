from django.contrib import admin

from .models import Product, Section


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'date_of_receipt', 'price', 'unit', 'provider_name')
    list_display = ('name', 'date_of_receipt', 'price', 'unit', 'provider_name')


class SectionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Section, SectionAdmin)
