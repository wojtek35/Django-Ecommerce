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
