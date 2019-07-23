import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class SignUpHandler(webbapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/sign_up.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class ProfileHandler(webbapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/profile.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class CreateHandler(webbapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/create.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class ViewMessagesHandler(webbapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/view_messages.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())

class PlayGameHandler(webbapp2.RequestHandler):
    def get(self):
        index_template = jinja_env.get_template('templates/play_game.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(index_template.render())


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/sign_up', SignUpHandler),
    ('/profile', ProfileHandler),
    ('/create', CreateHandler),
    ('/view_messages' ViewMessagesHandler),
    ('/play_game', PlayGameHandler),
], debug=True)
