'''
Created on Dec 1, 2012

@author: mark
'''



from google.appengine.api import memcache



def mems(key,val):
    memcache.set(key, val) #@UndefinedVariable why?
def memg(key):
    return memcache.get(key) #@UndefinedVariable works though