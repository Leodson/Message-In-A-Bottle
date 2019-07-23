import jinja2
import os
import webapp2
from google.appengine.api import users
import models
import random

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class ProfileHandler(webbapp2.RequestHandler):
    def get(self):
        profile_template = jinja_env.get_template('templates/profile.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(profile_template.render())

class CreateHandler(webbapp2.RequestHandler):
    def get(self):
        create_template = jinja_env.get_template('templates/create.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(create_template.render())

    def post(self):
        curr_message_txt = self.request.get('message')
        user = user.get_current_user()

        possible_recievers = User.query.fetch()
        num_possible_recievers = len(possible_recievers)
        rand_reciever = possible_recievers[random.randInt(0, num_possible_recievers - 1)]
        while rand_reciever.email_address == user:
            rand_reciever = possible_recievers[random.randInt(0, num_possible_recievers - 1)]

        curr_message = Message(
            message_txt = curr_message_txt,
            sender = user,
            reciever = rand_reciever
            )

        curr_message.put()


class ViewMessagesHandler(webbapp2.RequestHandler):
    def get(self):
        view_messages_template = jinja_env.get_template('templates/view_messages.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(view_messages_template.render())

class PlayGameHandler(webbapp2.RequestHandler):
    def get(self):
        play_game_template = jinja_env.get_template('templates/play_game.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(play_game_template.render())


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/sign_up', SignUpHandler),
    ('/profile', ProfileHandler),
    ('/create', CreateHandler),
    ('/view_messages' ViewMessagesHandler),
    ('/play_game', PlayGameHandler),
], debug=True)
