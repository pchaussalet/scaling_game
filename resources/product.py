from flask import request, redirect, make_response
from flask.ext import restful

from repository.product import ProductRepository
repo = ProductRepository()

class ProductListResource(restful.Resource):
  def get(self):
    return repo.list()

  def put(self):
    prod_id = repo.set(request.json)
    return prod_id, 201

class ProductResource(restful.Resource):
  def ensure_product_exists(self, prod_id):
    if not repo.exists(prod_id):
      restful.abort(404)
    return repo.get(prod_id)

  def get(self, prod_id):
    return self.ensure_product_exists(prod_id)

  def post(self, prod_id):
    self.ensure_product_exists(prod_id)
    return repo.set(prod_id, request.json)

  def delete(self, prod_id):
    self.ensure_product_exists(prod_id)
    repo.rm(prod_id)
    return '', 204

def register(api):
  api.add_resource(ProductListResource, '/product')
  api.add_resource(ProductResource, '/product/<string:prod_id>')
