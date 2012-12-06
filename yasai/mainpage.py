'''
Created on Dec 1, 2012

@author: mark
'''
import webapp2
from envdef import Handler
from dbfunc import getInventory, createItem


HTML_TEMPLATE = "mainpage.html"


class MainPage(Handler):
    def get(self, arg):
        user = self.testCookie()
        if not user:
            self.redirect("/login")
        inventory = getInventory()
        self.render(HTML_TEMPLATE, inventory=inventory, user=user)
        
    def post(self, arg):
        storeName= self.request.get("storeName")
        itemName = self.request.get("itemName")
        price = self.request.get("price")
        createItem(storeName, itemName, int(price))
        self.redirect("/")
        
app = webapp2.WSGIApplication([('/(.*)', MainPage)], debug=True)