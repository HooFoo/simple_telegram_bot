import sqlite3

class Storage:
    
    instance = Storage()
    
    def __init__():
        self.conn = sqlite3.connect('db/small.db')
        
        
    def save(self,table,data):
        conn.execute("create table if not exists %(table)s (id integer,data string)")
                
    def load(self,table, when):
        """достаем"""
        
def instance():
    return Storage.instance
