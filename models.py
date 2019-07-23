from google.appengine.ext import ndb

class User(ndb.Model):
    user_name = ndb.StringProperty()
