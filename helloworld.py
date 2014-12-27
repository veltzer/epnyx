import webapp2 # for WSGIApplication, RequestHandler
import jinja2 # for Environment, FileSystemLoader
import os.path # for dirname

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True,
)

class MainPage(webapp2.RequestHandler):
	def get(self):
		'''
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello, World!')
		'''
		template_values = {}
		template = JINJA_ENVIRONMENT.get_template('templates/index.jinja')
		self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
