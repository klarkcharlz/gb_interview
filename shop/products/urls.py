from django.urls import path

from .views import ProductsList

app_name = 'products'

urlpatterns = [
    path('', ProductsList.as_view(), name="products_list"),
]
