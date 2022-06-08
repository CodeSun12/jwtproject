import json

import requests

URL = "http://127.0.0.1:8000/refreshtoken/"

data = {
    "username": "superuser",
    "password": "superuser"
}

refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDc4MzgxMywiaWF0IjoxNjU0Njk3NDEzLCJqdGkiOiJkZGUwMjA4YzJlNTQ0MmNiYmNlNTZkMDMzNTA2ODQ4ZiIsInVzZXJfaWQiOjF9.8c9WGh17fLR4kiCoW1xYUSFKqRhILRdzZsXJBbiAOfU"

json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}

response = requests.post(
    url=URL,
    data=json_data,
    headers={'Content-Type': 'application/json',
             'Authorization': 'refresh {}'.format(refresh_token)})
data = response.json()
print(data)