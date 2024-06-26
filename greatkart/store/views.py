# from django.shortcuts import render,get_object_or_404
# from store.models import Product
# from category.models import Category
# # Create your views here.

# def store(request,category_slug = None):
#     categories = None
#     products = None
    
#     if category_slug != None:
#         categories = get_object_or_404(category, slug = category_slug)
#         products = Product.objects.filter(Category = categories, is_available = True)
#         product_count = products.count()
#     else:
#         products = Product.objects.all().filter(is_available = True)
#         product_count = products.count()

#     context = {
#             'products' : products,
#             'product_count':product_count,
#     }
#     return render(request,'store.html',context)


from carts.models import Cart,cartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        paginator = Paginator(products,6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        product_count = products.count()
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store.html', context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug= category_slug,slug = product_slug)
        in_cart = cartItem.objects.filter(cart__cart_id=_cart_id(request),product = single_product).exists()
    except Exception:
        raise Exception

    context = {

        'single_product': single_product,
        'in_cart':in_cart
    }

    return render(request,'product-detail.html',context)

def search(request):
    products = None  
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter( Q(product_description__icontains=keyword) | Q(product_name__icontains = keyword))
            product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count,
    }
    return render(request,'store.html',context)

