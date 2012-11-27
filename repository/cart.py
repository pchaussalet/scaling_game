class CartRepository(object):
  carts = {0: [0, 1], 1: [0], 2: [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
  def list(self):
    return self.carts
  
  def get(self, cart_id):
    return self.carts[cart_id]

  def exists(self, cart_id):
    return cart_id in self.carts.keys()
