from flask.ext import restful

from repository.cart import CartRepository
cart_repo = CartRepository()

from repository.product import ProductRepository
prod_repo = ProductRepository()

from service.deal import DealService
deal_serv = DealService()

VAT = 1.196

class CheckoutResource(restful.Resource):
  def ensure_cart_exists(self, cart_id):
    if not cart_repo.exists(cart_id):
      restful.abort(404)
    return cart_repo.get(cart_id)

  def ensure_product_exists(self, prod_id):
    if not prod_repo.exists(prod_id):
      restful.abort(404)
    return prod_repo.get(prod_id)

  def get(self, cart_id):
    cart = self.ensure_cart_exists(cart_id)
    total = 0
    for product_id in cart:
      product = self.ensure_product_exists(product_id)
      total += product['price']
    deals = deal_serv.compute(cart_id)
    deal_amount = 1
    for deal in deals.values():
      deal_amount -= deal
    total = total*deal_amount
    return round(total*VAT, 2)

def register(api):
  api.add_resource(CheckoutResource, '/checkout/<int:cart_id>')
