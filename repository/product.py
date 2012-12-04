from repository.mongo import Mongo

class ProductRepository(object):
  mongo = Mongo('localhost:27017', 'products')
  def list(self):
    return self.mongo.list()

  def exists(self, prod_id):
    return self.mongo.exists({'_id': prod_id})

  def get(self, prod_id):
    return self.mongo.get(prod_id)

  def set(self, data):
    return self.mongo.save(data)

  def rm(self, prod_id):
    self.mongo.delete(prod_id)
