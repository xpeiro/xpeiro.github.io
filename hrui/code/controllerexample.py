# import pymongo mongodb driver
import pymongo
from pymongo import MongoClient

#MongoDB setup (local)
mongoclient = MongoClient("127.0.0.1")
db = mongoclient.hrui
data = db.data
#end MongoDB setup