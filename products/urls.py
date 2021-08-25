from django.urls import path
from .views import all_products, product_detail, all_categories


urlpatterns = [
    path('', all_products, name='all_products'),
    path('details/<id>/', product_detail, name='product'),
    path('categories/', all_categories, name='all_categories')

]