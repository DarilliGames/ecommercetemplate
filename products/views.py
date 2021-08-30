from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q
from django.db.models.functions import Lower



def all_products(request):
    products = Product.objects.all()

    # init filter criteria
    query = None
    categories = None
    sub_categories = None
    sort = None
    direction = None

    # Check if filter criteria passed through
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            cat_query = Q(category__name__in=categories) | Q(category__category__name__in=categories)
            products = products.filter(cat_query)
            sub_categories  = SubCategory.objects.filter(name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == "name":
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sub_categories': sub_categories,
        'current_sorting': current_sorting
    }

    return render(request, 'all_products.html', context)

# Single Product
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        return render(request, "a_product.html", {"product": product})
    except Product.DoesNotExist:
        return redirect("all_products")
    
    return redirect("all_products")

# All Categories for easy sorting
def all_categories(request):
    categories = Category.objects.all()
    return render(request, "all_categories.html", {"categories": categories})

