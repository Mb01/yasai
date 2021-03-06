'''
Created on Dec 2, 2012

@author: mark
'''
from dbfunc import createItem, getInventory
from envdef import *  #@UnusedWildImport 


def_template = "additem.html"

class AddItem(Handler):
    def get(self):
        self.render(def_template)
        
    def post(self):
        arg = {}
        arg['itemname'] = self.request.get("itemname")
        arg['storename'] = self.request.get("storename")
        
        arg['price'] = self.request.get("price")
        
        arg['error_itemname'] = arg['error_storename'] = arg['error_price'] = ""
                
        #Check if entered all three

        if not arg['itemname']:
            arg['error_itemname'] = "enter item name"
        if not arg['storename']:
            arg['error_storename'] = "enter store name"
        if not arg['price']:
            arg['error_price'] = "enter price"
        
        #other checks
         
        if not arg['price'].isdigit():
            arg['error_price'] = "price must be a number"
        else:
            arg['price'] = int( arg['price'])
        if arg['error_itemname'] or arg['error_storename'] or arg['error_price']:
            self.render(def_template, **arg)
        else:
            #function returns error string if no such store exists.
            arg['error_storename'] = createItem(arg['storename'], arg['itemname'], arg['price'])
            getInventory(update=True)
        if arg['error_storename']:
            self.render(def_template, **arg)
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([('/additem', AddItem)], debug=True)