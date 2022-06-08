import json

import requests

URL = "http://127.0.0.1:8000/gettoken/"

data = {
    "username": "superuser",
    "password": "superuser"
}

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}

response = requests.post(url=URL, data=json_data, headers=headers)
data = response.json()
print(data)