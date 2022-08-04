from store.models import Product
from decimal import Decimal


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        '''
        Adding and updating the users session data
        '''
        product_id = str(product.id)
        qty = qty

        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': str(product.price),
                'qty': int(qty),
            }
        elif product_id in self.basket:
            old_qty = self.basket[product_id]['qty']
            qty = int(old_qty) + int(qty)
            self.basket[product_id]['qty'] = qty

        self.session.modified = True

    def __iter__(self):
        """
        Collent the product_id in the session data to query the database and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            if 'product' in item:
                yield item

    def __len__(self):
        '''
        Get the basket data anad count the qty of items
        '''
        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.basket.values())
