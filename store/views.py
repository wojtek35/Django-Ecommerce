from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    context = {
        'products': products

    }
    return render(request, 'store/index.html', context)


def product_detail_page(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        "product": product
    }
    return render(request, 'store/pdp.html', context)


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store/category.html', context)
