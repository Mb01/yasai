'''
Created on Dec 1, 2012

@author: mark
'''
from envdef import *
from dbdef import *


HTML_TEMPLATE = "mainpage.html"


class MainPage(Handler):
    def get(self, arg):
        self.render(HTML_TEMPLATE)
        self.response.out.write(self.testCookie())

app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)