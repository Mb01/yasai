'''
Created on Dec 1, 2012

@author: mark
'''
import logging
from secrets import makeHash, testHash

from google.appengine.ext import db #@UnresolvedImport don't worry be happy

class Store(db.Model):
    name = db.StringProperty(required=True)
    location = db.GeoPtProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)
    
class Item(db.Model):
    name = db.StringProperty(required=True)
    price = db.IntegerProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)
    
class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)

def createItem(store, name, price):
    parent = Store.all().filter("name =", store).get()
    if not parent:
        return "No such store found."
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

def createStore(name):
    check = Store.all().filter("name =", name).get()
    if check:
        return "store of that name exists"
    else:
        a = Store(name=name)
        a.put()

def createUser(username, password, email=None):
    password = makeHash(password)
    if email:
        user = User(username=username, password=password, email=email)
    else:
        user = User(username=username, password=password)
    user.put()
    message = "user: " + username + " created."
    logging.info(message)
    return message

def checkLogin(username, password):
    pass

    
    
