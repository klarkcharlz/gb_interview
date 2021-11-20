from django.views.generic.list import ListView

from .models import Product


# Create your views here.
class ProductsList(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data()
        context['title'] = 'Товары'
        return context
