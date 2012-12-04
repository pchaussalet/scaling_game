from flask.ext import restful

from service.deal import DealService
deal_serv = DealService()

from service.game import slowdown

class DealResource(restful.Resource):
  def get(self, cart_id):
    slowdown(.5)
    return deal_serv.compute(cart_id)

def register(api):
  api.add_resource(DealResource, '/deal/<string:cart_id>')

