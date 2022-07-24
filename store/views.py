from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products

    }
    return render(request, 'store/home.html', context)


def product_detail_page(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        "product": product
    }
    return render(request, 'store/products/pdp.html', context)
