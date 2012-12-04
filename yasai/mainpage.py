'''
Created on Dec 1, 2012

@author: mark
'''
from envdef import *
from dbfunc import *


HTML_TEMPLATE = "mainpage.html"


class MainPage(Handler):
    def get(self, arg):
        variables = {}
        if not self.testCookie():
            self.redirect("/login")
        
        
        self.render(HTML_TEMPLATE, **variables)
        
        
app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)