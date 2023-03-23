from flask import Flask,request
import json
import pymongo
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.2jnewlw.mongodb.net/?retryWrites=true&w=majority")
db = client.tut7 #Choose the DB

@app.route('/getMethod', methods=['GET'])
def getMethod():
    userCollection = db.Users                                           #choose our collection
    results = userCollection.find({},{'_id':0})                         #execute our query
    listOfUsers = list(results)                                         #convert cursor to list 
    jsonList = json.dumps(listOfUsers)                                  #Convert to Json format 
    return jsonList  
