from flask import Flask
from flask.ext import restful

from resources import product
from resources import cart
from resources import checkout

app = Flask(__name__)
api = restful.Api(app)

product.register(api)
cart.register(api)
checkout.register(api)

if __name__ == '__main__':
  app.run(debug=True)
