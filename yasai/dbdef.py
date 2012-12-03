'''
Created on Dec 1, 2012

@author: mark
'''

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



    
    
