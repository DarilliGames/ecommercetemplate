from django.urls import path
from .views import all_products, product_detail, all_catagories


urlpatterns = [
    path('', all_products, name='all_products'),
    path('<id>', product_detail, name='product'),
    path('categories', all_catagories, name='all_catagories')

]