from django.urls import path
from .views import (view_cart, add_to_cart, update_item_cart,
                    remove_item_cart, clear_cart)


urlpatterns = [
    path('', view_cart, name='cart'),
    path('add/<id>/', add_to_cart, name='add_to_cart'),
    path('update/<id>', update_item_cart, name='update_item_cart'),
    path('remove/<id>', remove_item_cart, name='remove_item_cart'),
    path('clear/', clear_cart, name='clear_cart'),

]
