'''
Created on Dec 2, 2012

@author: mark
'''
from dbdef import * #@UnusedWildImport don't worry be happy
from envdef import * #@UnusedWildImport don't worry be happy
import re

def_template = "login.html"

class Login(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        self.response.headers.add_header('Set-Cookie',str('username=%s;Path=/' % username ))


app = webapp2.WSGIApplication([('/login', Login)], debug=True)