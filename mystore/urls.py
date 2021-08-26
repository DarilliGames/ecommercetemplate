from django.contrib import admin
from django.urls import path, include

from home.views import get_index
# from products import urls as products_urls
# from checkout import urls as checkout_urls


urlpatterns = [
    path('', get_index, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),  
    path('products/', include('products.urls')),
] 