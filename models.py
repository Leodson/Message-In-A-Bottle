from google.appengine.ext import ndb

class User(ndb.Model):
    email_address = ndb.StringProperty()
    messages = ndb.KeyProperty(repeated = True)

class Message(ndb.Model):
    # CHARACTER_LIMIT = 200
    message_txt = ndb.TextProperty()
    sender = ndb.KeyProperty()
    opened = ndb.BooleanProperty()
    # ability to check if the message was viewed
