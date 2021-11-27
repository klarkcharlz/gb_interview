from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Product


# Create your views here.
class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    queryset = Product.objects.prefetch_related('section').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        section = self.kwargs.get('section_name', None)
        if section:
            context['object_list'] = Product.objects.prefetch_related('section').filter(section__name=section)
        context['title'] = 'Товары'
        return context
