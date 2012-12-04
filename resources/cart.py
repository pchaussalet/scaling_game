from flask import request
from flask.ext import restful

from repository.cart import CartRepository
cart_repo = CartRepository()

from repository.product import ProductRepository
prod_repo = ProductRepository()

from service.game import slowdown

class CartCreationResource(restful.Resource):
  def get(self):
    return cart_repo.list()  

  def put(self):
    cart_id = cart_repo.insert()
    return cart_id, 201

class CartResource(restful.Resource):
  def ensure_cart_exists(self, cart_id):
    if not cart_repo.exists(cart_id):
      restful.abort(404)
    return cart_repo.get(cart_id)

  def aggregate(self, cart):
    products = {}
    if cart.has_key('products'):
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

  def get(self, cart_id):
    cart = self.ensure_cart_exists(cart_id)
    slowdown(0.5)
    if 'aggregated' in request.args.keys():
      return self.aggregate(cart)
    return cart

  def post(self, cart_id):
    cart = self.ensure_cart_exists(cart_id)
    if not cart.has_key('products'):
      cart['products'] = []
    prod_id = request.json
    product = prod_repo.get(prod_id)
    cart['products'].append(product)
    cart_repo.save(cart)
    slowdown(0.5)
    return cart_id

def register(api):
  api.add_resource(CartCreationResource, '/cart')
  api.add_resource(CartResource, '/cart/<string:cart_id>')
