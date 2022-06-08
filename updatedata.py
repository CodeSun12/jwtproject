import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

data = {
    'id': 2,
    "name": "Abdul Rehman Khan",
    "roll_number": 105,
    "city": "Multan"
}

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Njk3NzEzLCJpYXQiOjE2NTQ2OTc0MTMsImp0aSI6IjY4OWM2MjNjMGE2ZTQ2ODg4YjcyMDg1MmE2YjU3Yzc4IiwidXNlcl9pZCI6MX0.D1u0KM60t9pEVLKT0r03oWzXGltPdAjsOemqrgzfXeY"
json_data = json.dumps(data)
response = requests.put(
    url=URL,
    data=json_data,
    headers={'Content-Type': 'application/json',
             'Authorization': 'Bearer {}'.format(access_token)})
data = response.json()
print(data)
