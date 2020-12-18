import requests, json, psycopg2
import dboperations
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def statusCheck():
    return "Status ok!"

@app.route('/fetchUser/<username>')
def getUser(username):
    return dboperations.fetchUser(username)

@app.route('/createUser', methods=['GET','POST'])
def createUser():
    userObj = request.data
    userObj = json.loads(userObj)
    print(userObj)
    res={}
    result = dboperations.createUser(userObj)
    res["Message"] = result
    print(res)
    return res

@app.route('/login', methods=['GET','POST'])
def userAuth():
    data = request.data
    data = json.loads(data)
    print(data)
    print(type(data))
    print(data)
    username = data['Username']
    password = data['Password']
    result = dboperations.userAuth(username, password)
    res = {}
    res["Message"] = result
    print(res)
    return res


@app.route('/updateUser', methods=['POST'])
def updateUser():
    data = request.data
    data = json.loads(data)
    print(data)
    result = dboperations.updateUser(data)
    res = {}
    res["Message"] = result
    return res

@app.route('/deleteUser/<username>', methods=['DELETE'])
def deleteUser(username):
    result = dboperations.delUser(username)
    res = {}
    res["Message"] = result
    print(res)
    return res





if __name__ == '__main__':
   app.run()