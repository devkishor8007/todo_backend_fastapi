from pymongo import MongoClient

class MongoConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient("mongodb://localhost:27017/")
        return cls._instance