from repository.cart import CartRepository
cart_repo = CartRepository()

from repository.product import ProductRepository
prod_repo = ProductRepository()

class DealService(object):
  def compute(self, cart_id):
    cart = cart_repo.get(cart_id)
    total = 0
    prod_count = 0
    for product_id in cart:
      product = prod_repo.get(product_id)
      total += product['price']
      prod_count += 1
    deal = {}
    if prod_count > 5:
      deal['count'] = .05
    if total > 150:
      deal['total'] = .15
    return deal
