
# coding: utf-8

# In[1]:

import pymongo


# In[2]:

client = pymongo.MongoClient()
db = client.test


# In[8]:

cursor = db.restaurants.find({"borough":"Manhattan"}and {"address.zipcode":"10019"} and {"grades.grade": "B"}).limit(10)
for document in cursor:
    print(document)


# In[9]:

cursor = db.restaurants.find({"grades.score":{"$gt":30}})
for document in cursor:
    print(document)


# In[4]:

import pymongo
cursor = db.restaurants.find().sort([
    ("borough",pymongo.ASCENDING),
    ("address.zipcode",pymongo.ASCENDING)
])
for document in cursor:
    print(document)


# In[5]:

from pymongo import MongoClient
client = MongoClient()
db = client.test


# In[9]:

result = db.restaurants.update_one(
    {"name":"Juni"},
    {
        "$set":{
            "cuisine":"American(New)"
        },
        "$currentDate":{"lastModified":True}
    }
)


# In[29]:

cursor = db.restaurants.find({"restaurant_id":"41704620"})
for document in cursor:
    print(document)


# In[16]:

print(result.matched_count)
print(result.modified_count)


# In[14]:

result = db.restaurants.update_one(
    {"restaurant_id":"41156888"},
    {"$set":{"address.street":"East 31st Street"}}
)


# In[19]:

result = db.restaurants.update_many(
    {"address.zipcode":"10016","cuisine":"Other"},
    {
        "$set":{"cuisine":"Category To Be Determined"},
        "$currentDate":{"lastModified":True}
    }
)


# In[30]:

print(result.matched_count)
print(result.modified_count)


# In[28]:

result = db.restaurants.replace_one(
    {"restaurant_id":"41704620"},
    {
        "name":"Vella 2",
        "address":{
            "coord":"[-73.9557413,40.7720266]",
            "building":"1480",
            "street":"2 Avenue",
            "zipcode":"10075"}
    }
)


# In[44]:

cursor = db.restaurants.aggregate(
    [
        {"$match":{"borough":"Queens","cuisine":"Brazilian"}},
        {"$group":{"_id":"$address.zipcode","count":{"$sum":1}}}
    ]
)


# In[45]:

for document in cursor:
    print(document)


# In[46]:

db.restaurants.create_index([("cuisine",pymongo.ASCENDING)])

