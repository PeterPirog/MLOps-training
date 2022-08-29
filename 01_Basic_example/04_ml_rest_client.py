import json
import requests

url = 'http://172.16.1.2:12320/model' # http://hpc.if.uz.zgora.pl:12320/

# First prediction
request_data = json.dumps({'age': 40, 'salary': 20000})
response = requests.post(url, request_data)
print(response.text)

# Second prediction
request_data = json.dumps({'age': 28, 'salary': 80000})
response = requests.post(url, request_data)
print(response.text)