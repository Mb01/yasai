'''
Created on Dec 1, 2012

@author: mark
'''
import logging

from google.appengine.ext import db #@UnresolvedImport don't worry be happy

class Store(db.Model):
    name = db.StringProperty(required=True)
    location = db.GeoPtProperty(required=False)

class Item(db.Model):
    name = db.StringProperty(required=True)
    price = db.IntegerProperty(required=False)
    
    
def createItem(store, name, price):
    parent = Store.all().filter("name =", store).get()
    item = Item.all().ancestor(parent.key()).filter("name =", name).get()
    if item:
        modifyItemPrice(store, name, price)
        logging.info("createItem call resulted in modify item of: " +store+" "+name+" "+str(price))
    else:
        item = Item(parent=parent, name=name,price=price)
        item.put()
        logging.info("item created" + store+" "+name+" "+str(price))

def modifyItemPrice(store, name, price):
    parent = Store.all().filter("name =", store).get()
    item = Item.all().ancestor(parent.key()).filter("name =", name).get()
    item.price = price
    item.put()
    

        