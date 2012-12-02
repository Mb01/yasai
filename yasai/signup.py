'''
Created on Dec 2, 2012

@author: mark
'''
from dbdef import * #@UnusedWildImport don't worry be happy
from envdef import * #@UnusedWildImport don't worry be happy
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
        
        error_username = error_password = error_verify = error_email = ""
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        PASS_RE = re.compile(r"^.{3,20}$")
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        
        if not (username and password and verify):
            error_username = "please fill in a username, password, and verify password"
        if not PASS_RE.match(password) and (not error_username):
            error_password = " invalid password"
        if not USER_RE.match(username) and (not error_username):
            error_username = " invalid username"
        if password != verify:
            error_verify = " password and verification do not match"
        logging.info("input was: " + username + " " + password + " " + verify + " " + email)
        
        if email and not EMAIL_RE.match(email):
            error_email = " not a valid email"
        if error_username or error_password or error_verify or error_email:
            self.render(def_template,
                        error_username = error_username,
                        error_password=error_password,
                        error_verify=error_verify,
                        error_email=error_email,
                        username=username,
                        email=email)
        else:
            if email:
                a = User(username=username,email=email,password=password)
                a.put()
            else:
                a = User(username=username,password=password)
                a.put()
            self.response.headers.add_header('Set-Cookie',str('username=%s;Path=/' % username ))
        
            self.redirect("/")

app = webapp2.WSGIApplication([('/signup', Signup)], debug=True)

