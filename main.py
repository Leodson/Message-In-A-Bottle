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

        curr_user = users.get_current_user()

        if curr_user:
            if not User.query(curr_user.nickname() == User.email_address).get():
                new_user_email_address = users.get_current_user().nickname()
                new_user = User(
                    email_address = new_user_email_address
                    )
                new_user.put()
            self.redirect('/profile')

        login_url = users.create_login_url('/')
        template_vars = {
            'login_url' : login_url
        }

        index_template = jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render(template_vars))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        logout_url = users.create_logout_url('/')

        template_vars = {
            'logout_url' : logout_url
        }

        profile_template = jinja_env.get_template('templates/profile.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(profile_template.render(template_vars))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        create_template = jinja_env.get_template('templates/create.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(create_template.render())

    def post(self):
        curr_message_txt = self.request.get('message')
        curr_user = user.get_current_user()

        possible_recievers = User.query.fetch()
        rand_reciever = random.choice(possible_recievers)
        while rand_reciever.email_address == curr_user.nickname():
            rand_reciever = random.choice(possible_recievers)

        curr_message = Message(
            message_txt = curr_message_txt,
            sender = curr_user,
            reciever = rand_reciever
            )

        rand_reciever.messages.append(curr_message.put())
        rand_reciever.put()

        self.redirect('/profile')

class ViewMessagesHandler(webapp2.RequestHandler):
    def get(self):

        curr_user_email_address = users.get_current_user().nickname()
        curr_user = User.query(curr_user_email_address == User.email_address).get()
        all_messages = curr_user.messages()

        first_20_char = []

        for message in all_messages:
            if len(message) > 20:
                first_20_char.append(message[0:20])
            else:
                first_20_char.append(message)

        template_vars = {
            'first_20_char' : first_20_char,
            'messages' : all_messages,
        }

        view_messages_template = jinja_env.get_template('templates/view_messages.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(view_messages_template.render(template_vars))

class PlayGameHandler(webapp2.RequestHandler):
    def get(self):
        play_game_template = jinja_env.get_template('templates/play_game.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(play_game_template.render())


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/profile', ProfileHandler),
    ('/create', CreateHandler),
    ('/view_messages', ViewMessagesHandler),
    ('/play_game', PlayGameHandler),
], debug=True)
