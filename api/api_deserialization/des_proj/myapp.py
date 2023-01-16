import requests
import json

URL = "http://127.0.0.1:8000/stddes/"
data = {
    'name':'Rahul',
    'roll':101,
    'city':'Dhaka'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
item = r.json()
print(r)
print(item)