import requests
import json
URL = "http://127.0.0.1:8000/student_details"

def get_data(id=None):
    data = {'id':id}
    jsonData = json.dumps(data)
    resData = requests.get(url=URL, data=jsonData)
    resData = resData.json()
    print(resData)

def post_data():
    data = {
        'name':'Rahul',
        'roll':199,
        'city':'Tangail'
    }
    # print(type(data))
    jsonData = json.dumps(data)
    # print(type(jsonData))
    resData = requests.post(url=URL, data=jsonData)
    resData = resData.json()
    print(resData)

def update_data():
    data = {
        'id':2,
        'name':'Rahul',
        'roll':108,
        'city':'Dhaka'
    }
    jsonData = json.dumps(data)
    resData = requests.put(url=URL, data=jsonData)
    resData = resData.json()
    print(resData)

def delete_data(id):
    data = {'id':id}
    jsonData = json.dumps(data)
    resData = requests.delete(url=URL, data=jsonData)
    resData = resData.json()
    print(resData)


# get_data()
# post_data()
update_data()
# delete_data(1)