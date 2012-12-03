'''
Created on Dec 2, 2012

@author: mark
'''
from dbdef import checkCred
from envdef import *


def_template = "login.html"

class Login(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        
        
        cred = checkCred(username, password)
        if cred:
            self.setCookie(username)
            


app = webapp2.WSGIApplication([('/login', Login)], debug=True)