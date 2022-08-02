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

    def __len__(self):
        '''
        Get the basket data anad count the qty of items
        '''
        return sum(item['qty'] for item in self.basket.values())
