from django.shortcuts import render, redirect
from products.models import Product


def view_cart(request):
    """Create your views here."""
    cart = request.session.get('cart', {})
    return render(request, "cart.html", {"cart": cart})


def add_to_cart(request, prod_id):
    """Adds item to cart.
    Should the item already be in the cart, it will add extras
    """
    try:
        Product.objects.get(pk=prod_id)
        if request.method == "POST":
            quantity = int(request.POST.get('quantity', 1))
        else:
            quantity = int(request.GET.get("quantity", 1))
        if quantity > 0:
            cart = request.session.get('cart', {})
            if prod_id in cart:
                cart[prod_id] += quantity
            else:
                cart[prod_id] = quantity
            request.session['cart'] = cart
            return redirect("product", prod_id)
        return redirect("product", prod_id)

    except Product.DoesNotExist:
        print(f"Product with ID {prod_id} does not exist")
        return redirect("all_products")

    return redirect("product", prod_id)



def update_item_cart(request, prod_id):
    """sets the quantity of a given item in the cart - positive or negative
    Will remove quantities of < 1"""
    try:
        Product.objects.get(pk=prod_id)
        cart = request.session.get('cart', {})
        if request.method == "POST":
            quantity = int(request.POST.get('quantity', 1))
        else:
            quantity = int(request.GET.get("quantity", 1))
        if quantity > 0:
            cart[prod_id] = quantity
            request.session['cart'] = cart
        else:
            if prod_id in cart:
                cart.pop(prod_id)
                request.session['cart'] = cart
        return redirect("product", prod_id)

    except Product.DoesNotExist:
        print(f"Product with ID {prod_id} does not exist")
        return redirect("all_products")

    return redirect("product", prod_id)


def remove_item_cart(request, prod_id):
    """
    removes all of a single item from the cart
    """
    cart = request.session.get('cart', {})
    if prod_id in cart:
        cart.pop(prod_id)
        request.session['cart'] = cart
    return redirect("cart")


def clear_cart(request):
    """
    Removes all items within Cart

    """
    request.session['cart'] = {}
    return redirect("cart")
