# import pymongo mongodb driver
import pymongo
from pymongo import MongoClient

#MongoDB setup (local)
mongoclient = MongoClient("127.0.0.1")
db = mongoclient.hrui
data = db.data
#end MongoDB setup

# read joystick item from database
joystick = data.find_one({"item": "joystick"})

#use joystick items
x = float(joystick['x'])
y = float(joystick['y'])
print("X: " + str(x))
print("Y: " + str(y))

# write robotData item
data.update({"item": "robotData"}, {"$set":{"position": {"x": x, "y": y}}})

# create new item (or update it if it exists)
data.update({"item": "newItem"}, {"$set":{"x": x, "y": y}}, upsert=True)