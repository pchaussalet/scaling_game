from flask import request
from flask.ext import restful

from repository.cart import CartRepository
repo = CartRepository()

class CartCreationResource(restful.Resource):
  def put(self):
    carts = repo.list()
    cart_id = max(carts.keys()) + 1
    carts[cart_id] = []
    return cart_id, 201

class CartResource(restful.Resource):
  def ensure_cart_exists(self, cart_id):
    if not repo.exists(cart_id):
      restful.abort(404)
    return repo.get(cart_id)

  def get(self, cart_id):
    return self.ensure_cart_exists(cart_id)

  def post(self, cart_id):
    cart = self.ensure_cart_exists(cart_id)
    prod_id = request.json
    cart.append(prod_id)
    return cart

def register(api):
  api.add_resource(CartCreationResource, '/cart')
  api.add_resource(CartResource, '/cart/<int:cart_id>')
