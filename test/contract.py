from unittest import TestCase, main

from httplib import HTTPConnection, ResponseNotReady

GET = 'GET'
DEBUG_LEVEL = 0

class ProductTest(TestCase):
  def setUp(self):
    self.conn = HTTPConnection('localhost', 5000, timeout=10)
    self.conn.set_debuglevel(DEBUG_LEVEL)

  def test_product_should_answer_200(self):
    self.conn.request(GET, '/product')
    response = self.conn.getresponse()
    self.assertEquals(response.status, 200)

  def test_product_id_should_answer_200(self):
    self.conn.request(GET, '/product/0')
    response = self.conn.getresponse()
    self.assertEquals(response.status, 200)


if __name__ == '__main__':
  import sys
  if '-d' in sys.argv:
    DEBUG_LEVEL = 2
    sys.argv.remove('-d')
  main()
