from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.db.models.functions import Lower



def all_products(request):
    products = Product.objects.all()

    # init filter criteria
    query = None
    categories = None
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
            products = products.filter(category__name__in=categories)
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
        'current_sorting': current_sorting
    }

    return render(request, 'all_products.html', context)

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    # product = get_object_or_404(Product, pk=id)
    return render(request, "a_product.html", {"product": product})

def all_catagories(request):
    catagories = Catagory.objects.all()
    return render(request, "all_catagories.html", {"catagories": catagories})

