'''
Created on Dec 2, 2012

@author: mark
'''
from dbdef import *
from envdef import *

def_template = "addstore.html"

class AddStore(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        arg = {}
        
        arg['storename'] = self.request.get("storename")
        
        arg['error_storename'] = ""
                
        #Check if a name was entered

        if not arg['storename']:
            arg['error_storename'] = "enter store name"
            self.render(def_template, **arg)
        else:
            arg['error_storename'] = createStore(arg['storename'])
        if arg['error_storename']:
            self.render(def_template, **arg)
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([('/addstore', AddStore)], debug=True)