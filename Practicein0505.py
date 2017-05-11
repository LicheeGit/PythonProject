# 这是Python2016 MongoDB的学习 来自https://docs.mongodb.com/getting-started/python/client/
# 同时学习了http://python.jobbole.com/87157/ 的内容，非常好(原来就是前一个页面的翻译。。囧

from pymongo import MongoClient
from datetime import datetime

client = MongoClient()  # default runs on the localhost interface on port 27017

db = client.test
coll = db.dataset

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "buiding": "1480",
            "coord": [-73.9557413, 407720266]
        },
        "borough":"Manhattan",
        "cuisine":"Italian",
        "grades":[
            {
                "date":datetime.strptime("2014-10-01","%Y-%m-%d"),
                "grade":"B",
                "score":17
            }
        ],
        "name":"Vella",
        "restaurant_id":"41704620"
    }
)
print("ObjectId:({0})".format(str(result.inserted_id)))
