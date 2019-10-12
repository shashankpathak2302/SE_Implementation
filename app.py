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

@app.route('/update_calendar',methods=['POST'])
def update_calendar_info():
    deptId = request.json["dept_id"]
    eType = request.json["e_type"]
    client = MongoClient()
    db = client['employee_management_db']
    department_details = db.department_table
    res = list(department_details.find({'dept_id':deptId}))
    if(len(res) == 0):
        client.close()
        return jsonify({}),400
    calendar_details = db.calendar_table
    res = list(calendar_details.find({'dept_id':deptId,'e_type':eType}))
    cas = request.json['casual']
    ear = request.json['earned']
    med = request.json['medical']
    if(len(res) != 0):
        calendar_details.update_one({'dept_id':deptId,'e_type':eType},{"$set": {'casual':cas,'earned':ear,'medical':med}})
        client.close()
        return jsonify({}),200
    data = {'dept_id':deptId,'e_type':eType,'casual':cas,'earned':ear,'medical':med}
    calendar_details.insert_one(data)
    client.close()
    return jsonify({}),200

#has to be changed
@app.route('/login',methods=['POST'])
def check_login():
    usr = request.json["user_name"]
    password = request.json["password"]
    client = MongoClient()
    db = client['employee_management_db']
    ld = db.login_table
    res = ld.find({'user_name':usr})
    for i in res:
        if(i['user_name'] == usr and i['password'] == password):
            client.close()
            return jsonify({}),200
    client.close()
    return jsonify({}),400
if __name__ == '__main__':
    app.run("0.0.0.0",port=5000)
