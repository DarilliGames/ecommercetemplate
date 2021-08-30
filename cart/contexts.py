from products.models import Product

def cart_context(request):

    cart = request.session.get('cart', {})
    num_items = 0
    total = 0
    cart_items = []
    for item, quantity in cart.items():
        try:
            product = Product.objects.get(pk = item)
            num_items = quantity
            sub_total = product.price*quantity
            cart_items.append({
                "product": product,
                "quantity": quantity,
                "total": sub_total
            })
            total += sub_total
        except Product.DoesNotExist:
            cart.pop(item)
            request.session["cart"] = cart
    
    context = {
        "num_items": num_items,
        "total": total,
        "cart_items": cart_items
    }
    print(context)

    return context
