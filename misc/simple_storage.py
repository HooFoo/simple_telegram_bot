import shelve

class Storage:
    
    instance = Storage()
    
    def __init__():
        self.db = shelve.open('db/small.db')
        
        
    def save(self,key,value):
        self.db[key] = value
        
                
    def load(self,key):
        return self.db[key]
    
    def keys(self):
        return self.db[key]

    def clean(self,key):
        del self.db[key]
        
def instance():
    return Storage.instance
