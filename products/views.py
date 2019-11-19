from django.shortcuts import render, get_object_or_404
from .models import *


def all_products(request):
    products = Product.objects.all()
    return render(request, "all_products.html", {"products": products})

def a_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "a_product.html", {"product": product})

def all_catagories(request):
    catagories = Catagory.objects.all()
    return render(request, "all_catagories.html", {"catagories": catagories})

def a_catagory(request, id):
    catagory = get_object_or_404(Catagory, pk=id)
    return render(request, "a_product.html", {"catagory": catagory})