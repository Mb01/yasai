'''
Created on Dec 3, 2012

@author: mark
'''
import logging
from secrets import makeHash, testHash
from dbdef import *

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
    exists = User.all().filter("username =", username).get()
    if exists:
        return "User " + username + " taken."
    if email:
        user = User(username=username, password=password, email=email)
    else:
        user = User(username=username, password=password)
    user.put()
    logging.info(username + " created!")

def checkCred(username, password):
    user = User.all().filter("username =", username).get()
    if user:
        passMatch = testHash(user.password, password)
        return passMatch
    return False