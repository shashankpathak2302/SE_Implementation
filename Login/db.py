from pymongo import MongoClient
client = MongoClient()
db = client['trial']
ld = db.login_details
res = ld.find_one({'username':'shashank'})
print(res)
client.close()
