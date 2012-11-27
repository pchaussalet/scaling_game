from flask.ext import restful

from service.deal import DealService
deal_serv = DealService()

class DealResource(restful.Resource):
  def get(self, cart_id):
    return deal_serv.compute(cart_id)

def register(api):
  api.add_resource(DealResource, '/deal/<int:cart_id>')

