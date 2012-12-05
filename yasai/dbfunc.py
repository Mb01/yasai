'''
Created on Dec 3, 2012

@author: mark
'''
import logging
from secrets import makeHash, testHash
from dbdef import Store, Item, User
from cache_util import mems, memg
### multi functions
def getInventory():
    inventory = memg("_inventory123")
    if not inventory:
        logging.info("inventory hits db")
        inventory = {}
        stores = Store.all()
        for store in stores:
            inventory[store.name] = {}
            items = Item.all().ancestor(store.key())
            for item in items:
                item = item.asDict()
                inventory[store.name][item["name"]] = item
        mems("_inventory123", inventory)
    else:
        logging.info("inventory hits cache")
    return inventory
    
###item functions

def createItem(store, name, price):
    parent = Store.all().filter("name =", store).get()
    if not parent:
        return "No such store found."
    item = Item.all().ancestor(parent.key()).filter("name =", name).get()
    if item:
        _modifyItemPrice(store, name, price)
        logging.info("createItem call resulted in modify item of: " +store+" "+name+" "+str(price))
    else:
        item = Item(parent=parent, name=name,price=price, store=store)
        item.put()
        logging.info("item created" + store+" "+name+" "+str(price))

def _modifyItemPrice(store, name, price):
    '''create item uses this function if item found'''
    #so error checking is done by createItem
    parent = Store.all().filter("name =", store).get()
    item = Item.all().ancestor(parent.key()).filter("name =", name).get()
    item.price = price
    item.put()
    

###store functions
def createStore(name):
    check = Store.all().filter("name =", name).get()
    if check:
        return "store of that name exists"
    else:
        a = Store(name=name)
        a.put()

###user functions
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
