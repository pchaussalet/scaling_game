from repository.mongo import Mongo

class CartRepository(object):
  mongo = Mongo('localhost:27017', 'carts')
  carts = {0: [0, 1], 1: [0], 2: [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
  def list(self):
    return self.mongo.list()

  def exists(self, cart_id):
    return self.mongo.exists({'_id': cart_id})

  def get(self, cart_id):
    return self.mongo.get(cart_id)

  def insert(self):
    return self.mongo.save({})

  def save(self, data):
    return self.mongo.save(data)
