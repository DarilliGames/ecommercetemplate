from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get("cart", {})
    if cart != {}:
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = Order.save(commit=False)
                for id, quantity in cart.items():
                    try:
                        product = Product.objects.get(pk=item)
                        if isinstance(id, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                        order_line_item.save()
                    except Product.DoesNotExist:
                        print(f"Product {id} does not exist")
                    except:
                        print("Something went wrong - unprecise")
                # Currently will not correctly save due to fields being left blank
                order.save()
                print("Got Post")
        else:
            form = OrderForm()
        context = {
            "form": form 
            
        }
        
        return render(request, "checkout.html", context)        
    else:
        return redirect("all_products")