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

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/sign_up', SignUpHandler),
], debug=True)
