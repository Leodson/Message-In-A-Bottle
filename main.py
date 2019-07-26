from google.appengine.api import users
from models import User, Message
import jinja2
import os
import random
import webapp2

# for each Handler, make sure that it only executes if they are actually signed in
# Make sure that they can only click create message if it is not blank

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        curr_user = users.get_current_user()

        if curr_user:
            if not User.query(User.email_address == curr_user.email()).get():
                new_user_email_address = curr_user.email()
                new_user = User(
                    email_address = new_user_email_address,
                    messages = []
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
        new_message_txt = self.request.get('message')
        curr_user = User.query(User.email_address == users.get_current_user().email()).get()

        possible_recievers = User.query(User.email_address != curr_user.email_address).fetch()
        # if len(possible_recievers) <= 1:
        #     rand_reciever = curr_user
        # else:
        #     rand_reciever = random.choice(possible_recievers)
# just to test
        rand_reciever = curr_user

        curr_message = Message(
            message_txt = new_message_txt,
            sender = curr_user.key,
            opened = False
            )

        rand_reciever.messages.append(curr_message.put())
        rand_reciever.put()

        self.redirect('/profile')

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        create_template = jinja_env.get_template('templates/about.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(create_template.render())

class ViewMessagesHandler(webapp2.RequestHandler):
    def get(self):
        curr_user = User.query(User.email_address == users.get_current_user().email()).get()
        message_keys = curr_user.messages

        message_txts = [str(key.get().message_txt) for key in message_keys]
        print(message_txts)
        first_50_char = [txt[0:60] if len(txt) > 60 else txt for txt in message_txts]
        #print(first_20_char)

        template_vars = {
            'first_20_char' : first_50_char,
            'messages' : message_txts,
        }

        view_messages_template = jinja_env.get_template('templates/view_messages.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(view_messages_template.render(template_vars))

class PlayGameHandler(webapp2.RequestHandler):
    def get(self):
        curr_user = User.query(User.email_address == users.get_current_user().email()).get()
        all_message_keys = curr_user.messages
        unopened_message_keys = [key for key in all_message_keys if key.get().opened == False]

        template_vars = {
            'messages' : unopened_message_keys
        }

        play_game_template = jinja_env.get_template('templates/game.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(play_game_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/profile', ProfileHandler),
    ('/create', CreateHandler),
    ('/view_messages', ViewMessagesHandler),
    ('/play_game', PlayGameHandler),
    ('/about', AboutHandler)
], debug=True)
