import json

import requests

URL = "http://127.0.0.1:8000/studentapi/"

data = {
    "name": "Bilal Khan",
    "roll_number": 105,
    "city": "Multan"
}

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0Njk3MjgyLCJpYXQiOjE2NTQ2OTAzNTIsImp0aSI6IjAyMmUxOWU1MWUzODQ1ODA5OTFlMzNmMTZiMDA4NTk5IiwidXNlcl9pZCI6MX0.SV49rTudM_HvuApc-0O6Ej46M45OmSVCgtYXpTYAtR0"

json_data = json.dumps(data)
response = requests.post(
    url=URL,
    data=json_data,
    headers={'Content-Type': 'application/json',
             'Authorization': 'Bearer {}'.format(access_token)})
data = response.json()
print(data)
