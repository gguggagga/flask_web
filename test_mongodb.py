from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:1234@cluster0.4dhoo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

list = db.mydata
list.insert_one({"data":"test","asfads":"sadfasd","asfdasf":"asdfadsf"})
