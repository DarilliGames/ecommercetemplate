from django.conf.urls import url
from .views import all_products, a_product, all_catagories, a_catagory


urlpatterns = [
    url(r'^products/', all_products, name='all_products'),
    url(r'^product/(\d+)', a_product, name='product'),

    url(r'^catagories/', all_catagories, name='all_catagories'),
    url(r'^catagory/(\d+)', a_catagory, name='catagory'),

]