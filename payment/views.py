from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
import stripe


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51LXnpAF2ppp8RarrYSc4DYQlyhySWTux1vi7GUfCcInq65Z9C0kNoUzt3sf6C4fzCliENhckinWct152CDkhTq4L00IU41tLz4'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={
            'userid': request.user.id
        }
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


@login_required
def order_placed(request):
    return render(request, 'payment/order_placed.html')
