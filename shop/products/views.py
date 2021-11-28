from django.views.generic.list import ListView
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from .models import Product


# Create your views here.
class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'
    queryset = Product.objects.prefetch_related('section').filter(site__id=settings.SITE_ID)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        section = self.kwargs.get('section_name', None)
        if section:
            context['object_list'] = Product.objects.prefetch_related('section').\
                filter(section__name=section, site__id=get_current_site(self.request).id)
        context['title'] = 'Товары'
        return context
