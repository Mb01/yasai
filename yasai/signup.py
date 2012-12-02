'''
Created on Dec 2, 2012

@author: mark
'''
from dbdef import *
from envdef import *
import re

def_template = "signup.html"

class Signup(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        error = ""
        if not (username and password and verify):
            error += "please fill in a username, password, and verify password"
        
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASS_RE = re.compile(r"^.{3,20}$")
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")        

        if not USER_RE.match(username):
            error += " invalid username"
        if not PASS_RE.match(password):
            error += " invalid password"
        if password != verify:
            error += " password and verification do not match"
        logging.info("input was: " + username + " " + password + " " + verify + " " + email)
        
        if email and not EMAIL_RE.match(email):
            error += " not a valid email"
        if error:
            logging.info(error)
            self.render(def_template, error=error, username=username, email=email)
        else:
            if email:
                a = User(username=username,email=email,password=password)
            else:
                a = User(username=username,password=password)
            self.response.headers.add_header('Set-Cookie',str('username=%s;Path=/' % username ))
        
            self.redirect("/welcome?username=" + username)

app = webapp2.WSGIApplication([('/signup', Signup)], debug=True)
