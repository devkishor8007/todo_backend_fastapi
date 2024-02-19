from apps.config.db import MongoConnection
from apps.models.todo import TodoModel

class Todo:
    def __init__(self):
        self.db = MongoConnection().client.test_database
        self.collection = self.db.todoss
    
    def find_all(self, query):
        return self.collection.find(query)
    
    def find_one(self, query):
        return self.collection.find_one(query)
    
    def create(self, todo: TodoModel):
        return self.collection.insert_one(dict(todo))
    
    def update_todo(self, id, todo: TodoModel):
        return self.collection.find_one_and_update({"_id": id}, {"$set": dict(todo)})
    
    def delete_one(self, query):
        return self.collection.find_one_and_delete(query)