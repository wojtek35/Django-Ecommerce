from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .basket import Basket
from store.models import Product


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        qty = request.POST.get('qty')
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=qty)

        '''
        get_object_or_404 method is basically:

        try:
            product = Products.objects.get(id='productid')
        except:
            raise Http404
        
        '''
        response = JsonResponse({
            'qty': qty
        })
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        response = JsonResponse({
            'Success': True
        })
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        qty = int(request.POST.get('product_qty'))
        basket.update(product=product_id, qty=qty)

        basket_qty = len(basket)
        basket_total = basket.get_total_price()
        print(basket_total)

        new_total = Decimal(basket.basket[str(product_id)]['price'])*qty
        response = JsonResponse({
            'new_item_total': new_total,
            'new_basket_qty': basket_qty,
            'new_basket_total': basket_total
        })
        return response
