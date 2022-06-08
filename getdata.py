import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

data = {
    "username": "superuser",
    "password": "superuser"
}

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Njk5NzYxLCJpYXQiOjE2NTQ2OTk0NjEsImp0aSI6IjJlYWNlNzQ0NzYxOTQ4Nzk5ZGFlYzhkY2E1NzcyYTA4IiwidXNlcl9pZCI6MX0.0QzFxSN-nQZjYVYfM5tLM3kfI8xj2gVZ62G236XDfCs"
json_data = json.dumps(data)
response = requests.get(
    url=URL,
    data=json_data,
    headers={'Content-Type': 'application/json',
             'Authorization': 'Bearer {}'.format(access_token)})
data = response.json()
print(data)
