'''
Created on Dec 1, 2012

@author: mark
'''
import os
import webapp2
import jinja2
from secrets import makeCookieHash, testCookieHash

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

class Handler(webapp2.RequestHandler):
    """Extends request handler with custom functions"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
    
    def setCookie(self, username):
        cookieVal = "%s:%s" % (str(username), str(makeCookieHash(username)))
        self.response.set_cookie('user', cookieVal)
    def testCookie(self):
        cookie = self.request.cookies.get('user')
        
        if cookie and cookie.find(":") != -1:
            username, t_hash = cookie.split(':')
            if testCookieHash(t_hash, username):
                return username
            else:
                return False
        else:
            return False
    
    
    
    