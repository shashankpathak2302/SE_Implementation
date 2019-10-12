from flask import Flask, jsonify, request, abort
from pymongo import MongoClient
import requests
import re
import pickle
app = Flask(__name__)
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Origin','127.0.0.1')
  return response
 
@app.route('/check',methods=['GET'])
def trial_connection():
    trial_list = dict()
    trial_list["trial"] = "allOk";
    return jsonify(trial_list),200

@app.route('/login1',methods=['POST'])
def check_login():
    print("here")
    usr = request.json["username"]
    password = request.json["password"]
    client = MongoClient()
    db = client['trial']
    ld = db.login_details
    res = ld.find({'username':usr})
    for i in res:
        if(i['username'] == usr and i['password'] == password):
            return jsonify({}),200
    return jsonify({}),400
    client.close()
if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
