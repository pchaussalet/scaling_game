class ProductRepository(object):
  products = {0: {'name': 'Product one', 'price': 10}, 1: {'name': 'Product two', 'price': 20}}
  def list(self):
    return self.products

  def exists(self, prod_id):
    return prod_id in self.products.keys()

  def get(self, prod_id):
    return self.products[prod_id]

  def set(self, prod_id, data):
    self.products[prod_id] = data
    return self.get(prod_id)

  def rm(self, prod_id):
    del self.products[prod_id]
