from django.contrib import admin
from .models import Product, Catagory, FeaturedItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(FeaturedItem)