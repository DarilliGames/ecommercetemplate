from django.shortcuts import render, redirect, HttpResponse
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_context
from django.conf import settings

import stripe
import json

# Create your views here.
def checkout(request):
    cart = request.session.get("cart", {})
    if cart != {}:
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.stripe_pid = pid
                order.original_bag = json.dumps(cart)
                order.save()
                for id, quantity in cart.items():
                    try:
                        product = Product.objects.get(pk=id)
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                    except Product.DoesNotExist:
                        print(f"Product {id} does not exist")
                    except:
                        print("Something went wrong - unprecise")
                # Currently will not correctly save due to fields being left blank
                
                print("Got Post")
                return redirect("home")
        else:
            form = OrderForm()
            
            current_bag = cart_context(request)
            total = current_bag['total']
            stripe_total = round(total * 100)
            stripe.api_key = settings.STRIPE_SECRET_KEY
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency="eur",
            )
        context = {
            "form": form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret
        }
        
        return render(request, "checkout.html", context)        
    else:
        return redirect("all_products")

def cache_checkout_data(request):
    """
    Will be used to store data when the form gets submitted and payment is successful to be used in WHH.py
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        print(e)
        print("NOOOO")
        print(request.POST.get('client_secret').split('_secret')[0])
        # messages.error(request, 'Sorry, your payment cannot be \
        #     processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout_success(request, order_number):
    try:
        order = Order.objects.get(pk=order_number)
    except:
        return redirect("home")
    context = {
        "order": order
    }
    return render(request, "order.html", context)