from repository.cart import CartRepository
cart_repo = CartRepository()

from repository.product import ProductRepository
prod_repo = ProductRepository()

class DealService(object):
  def aggregate(self, cart):
    products = {}
    for product in cart['products']:
      if product['_id'] not in products.keys():
        products[product['_id']] = {'count': 0,
                                    'name': product['name'],
                                    'price': product['price'],
                                    'total': 0}
      products[product['_id']]['count'] += 1
      products[product['_id']]['total'] = products[product['_id']]['count'] * products[product['_id']]['price']

    return {'_id': cart['_id'],
            'products': products}

  def compute(self, cart_id):
    cart = cart_repo.get(cart_id)
    total = 0
    prod_count = 0
    deals = {}
    for product in cart['products']:
      product = prod_repo.get(product['_id'])
      total += product['price']
      prod_count += 1
    aggr_cart = self.aggregate(cart)
    if prod_count > 5:
      deals['Item count'] = .05
    if total > 1500:
      deals['Invoice total'] = .15
    subtotal = 0
    for product in cart['products']:
      subtotal += product['price']
    totaldeal = 0
    for deal in deals.values():
      totaldeal += deal
    discount = subtotal*totaldeal
    total = subtotal - discount
    aggr_cart['deals'] = deals
    aggr_cart['subtotal'] = subtotal
    aggr_cart['discount'] = discount
    aggr_cart['total'] = total
    return aggr_cart
