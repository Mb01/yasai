'''
Created on Dec 1, 2012

@author: mark
'''
import webapp2
from envdef import Handler
from dbfunc import getInventory


HTML_TEMPLATE = "mainpage.html"


class MainPage(Handler):
    def get(self, arg):
        variables = {}
        if not self.testCookie():
            self.redirect("/login")
        inventory = getInventory()
        
        self.render(HTML_TEMPLATE, inventory = inventory)
        
        
app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)