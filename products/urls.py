from django.urls import path
from .views import product_home, product_search, product_detail, all_categories


urlpatterns = [
    path('', product_home, name='product_home'),
    path('search', product_search, name='all_products'),
    path('details/<id>/', product_detail, name='product'),
    path('categories/', all_categories, name='all_categories')

]