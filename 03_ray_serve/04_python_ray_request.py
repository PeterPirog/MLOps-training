# http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
#
# run server firstredis stop
# pip install mlflow-ray-serve
# ray start --head
#
#mlflow models serve -m file:///G:/PycharmProject/MLOps-training/03_ray_serve/mlruns/0/34a261edacb844b8a5a31376dd25e189/artifacts/iris_rf

#
import requests
import json

url = "http://127.0.0.1:5000/invocations"
payload = "{\"columns\":[\"sepal length (cm)\"," \
          "\"sepal width (cm)\"," \
          "\"petal length (cm)\"," \
          "\"petal width (cm)\"],\"data\":[[5.1,3.5,1.4,0.2],[6.5,2.8,4.6,1.5],[6.5,3.0,5.8,2.2]]}"
headers = {
  'Content-Type': 'application/json',
  'format': 'pandas-split'
}

r = requests.request("POST", url, headers=headers, data=payload)
print(json.loads(r.text))

# reformated payload
url = "http://127.0.0.1:5000/invocations"
payload = '{"columns":["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"],' \
          '"data":[[5.1,3.5,1.4,0.2],[6.5,2.8,4.6,1.5],[6.5,3.0,5.8,2.2]]}'
headers = {
  'Content-Type': 'application/json',
  'format': 'pandas-split'
}

r = requests.request("POST", url, headers=headers, data=payload)
print(json.loads(r.text))