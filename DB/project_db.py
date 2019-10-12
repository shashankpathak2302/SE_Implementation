from pymongo import MongoClient
client = MongoClient()
db = client['employee_management_db']

#2.Login Collection
login_details = db.login_table
data1 = {'e_id':'2019DEV001','user_name':'Rahul','password':'E5857B335AFDF35CA81A110BC81F38682F8A89892CC597F5398DFEF82D42B513'}
data2 = {'e_id':'2019DEV002','user_name':'Raghav','password':'9425C3AE8CF81E1475108C7CA9ACF70B5DF3FEAB935C1910DD0E618FB431DDA0'}
data3 = {'e_id':'2019DEV003','user_name':'Sagar','password':'CFC2BB2D953B68C45D2711E542076A8F47C1A37778CF8A9CC117F087A5FDDE9F'}
login_details.insert_many([data1,data2,data3])

#4.Deapartment
dept_details = db.department_table
data = {'dept_id':'DEVBNG','hod_id':'2019DEV001','dept_name':'development','total_employees':'30','min_employees':'17'}
dept_details.insert_one(data)

#5.Calendar
calendar_details = db.calendar_table
data1 = {'dept_id':'DEVBNG','e_type':'DEV','casual':'8','earned':'10','medical':'6'}
data2 = {'dept_id':'DEVBNG','e_type':'MANAGER','casual':'10','earned':'12','medical':'8'}
data3 = {'dept_id':'DEVBNG','e_type':'HOD','casual':'12','earned':'14','medical':'10'}
calendar_details.insert_many([data1,data2,data3])

#1.Employee Collection
employee_details = db.employee_details_table
data1 = {'e_id':'2019DEV001','user_name':'Rahul','e_contact':'8887712120','e_email':'rahul@gmail.com','e_type':'HOD','dept_id':'DEVBNG','leave_left':{'casual':'12','earned':'14','medical':'10'},'approver_id':'2019DEV001'}
data2 = {'e_id':'2019DEV002','user_name':'Raghav','e_contact':'8898513120','e_email':'raghav123@gmail.com','e_type':'MANAGER','dept_id':'DEVBNG','leave_left':{'casual':'10','earned':'12','medical':'8'},'approver_id':'2019DEV001'}
data3 = {'e_id':'2019DEV003','user_name':'Sagar','e_contact':'9992212120','e_email':'sagar@gmail.com','e_type':'DEV','dept_id':'DEVBNG','leave_left':{'casual':'8','earned':'10','medical':'6'},'approver_id':'2019DEV002'}
employee_details.insert_many([data1,data2,data3])

#3.Leave Collection
leave_col = db.leave_collection_table
data = {'e_id':'2019DEV003','type':'medical','list_of_dates':['30/10/2019','31/10/2019'],'reason':'medical leave','status':'pending'}
leave_col.insert_one(data)






