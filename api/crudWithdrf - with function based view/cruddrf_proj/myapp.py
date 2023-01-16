import requests
import json


URL = "http://127.0.0.1:8000/student_details/"

def get_data(id=None):
    rdata = {}
    if id is not None:
        rdata = {'id':id}
    jsonData = json.dumps(rdata)
    res = requests.get(url=URL, data=jsonData)
    data = res.json()
    print(data)

def post_data():
    data = {
        'id':14,
        'name':'Rabib',
        'roll':22,
        'city':'Dinajpur'
    }
    jsonData = json.dumps(data)
    res = requests.post(url=URL, data=jsonData)
    msg_data = res.json()
    print(msg_data)

def put_data():
    data = {
        'id':2,
        # 'name':'Ridoy Khan',
        # 'roll':108,
        'city':'Chittagong'
    }

    json_data = json.dumps(data)
    res = requests.put(url=URL, data=json_data)
    msg_data = res.json()
    print(msg_data)

def delete():
    data = {'id':1}
    json_data = json.dumps(data)
    res = requests.delete(url=URL,data=json_data)
    res_data = res.json()
    print(res_data)


# get_data()
# post_data()
# put_data()
# delete()
