import requests
import json

URL = "http://127.0.0.1:8000/studentapi/1/"


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0NzAwMjIzLCJpYXQiOjE2NTQ2OTk5MjMsImp0aSI6Ijg2ZmIyYzkzOWI2YzRhNDg5YjQ5YzM4MDBkOTRkMDY2IiwidXNlcl9pZCI6MX0.yM6uzCMoIefUU3ERkctHLjio9ZBoh3V6P47GxkG-uNc"

response = requests.delete(
    url=URL,
    headers={'Content-Type': 'application/json',
             'Authorization': 'Bearer {}'.format(access_token)})
data = response.json()
print(data)
