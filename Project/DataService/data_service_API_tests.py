# https://www.w3schools.com/python/module_requests.asp
import requests

url = 'http://localhost:7071/api/CreateRecords'
document = {'datetime': '2023-09-22', 'title': 'test0', 'message' : '0th test'}     # or whatever your data fields are

x = requests.post(url, json=document)
print("response text", x.text)
print("response code", x.status_code)

document = {'name' : 'Alice'}
