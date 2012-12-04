from pymongo import Connection
from bson import ObjectId

class Mongo(object):
  conn = None
  def __init__(self, connection_string, collection):
    if self.conn == None:
      self.conn = Connection(connection_string)
    db = self.conn.scaling_game
    self.coll = db[collection]

  def _b2j(self, document):
    document['_id'] = str(document['_id'])
    return document

  def _j2b(self, document):
    if document.has_key('_id'):
      document['_id'] = ObjectId(document['_id'])
    return document

  def list(self, criterias={}):
    rs = []
    for doc in self.coll.find(criterias):
      rs.append(self._b2j(doc))
    return rs

  def get(self, _id):
    return self._b2j(self.coll.find_one(ObjectId(_id)))

  def exists(self, criterias):
    for criteria in criterias.keys():
      if criteria == '_id':
        criterias['_id'] = ObjectId(criterias['_id'])
    return self.coll.find(criterias).count() > 0

  def save(self, doc):
    return str(self.coll.save(self._j2b(doc)))

  def delete(self, _id):
    self.coll.remove(ObjectId(_id))
