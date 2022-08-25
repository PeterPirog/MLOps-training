#https://www.mlflow.org/docs/latest/models.html#model-signature-and-input-example
# https://github.com/ray-project/mlflow-ray-serve
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature



iris = datasets.load_iris()
iris_train = pd.DataFrame(iris.data, columns=iris.feature_names)
clf = RandomForestClassifier(max_depth=7, random_state=0)
clf.fit(iris_train, iris.target)

# get column names and datatypes from dataframe
signature = infer_signature(iris_train, clf.predict(iris_train))
# Or in alternative way
"""
from mlflow.models.signature import ModelSignature
from mlflow.types.schema import Schema, ColSpec

input_schema = Schema([
  ColSpec("double", "sepal length (cm)"),
  ColSpec("double", "sepal width (cm)"),
  ColSpec("double", "petal length (cm)"),
  ColSpec("double", "petal width (cm)"),
])
output_schema = Schema([ColSpec("long")])
signature = ModelSignature(inputs=input_schema, outputs=output_schema)
"""



mlflow.sklearn.log_model(clf, "iris_rf", signature=signature)

print(signature)

# mlflow models serve -m file:///G:/PycharmProject/MLOps-training/03_ray_serve/mlruns/0/34a261edacb844b8a5a31376dd25e189/artifacts/iris_rf

"""
https://www.mlflow.org/docs/latest/models.html#deploy-mlflow-models
curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{"columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)","petal width (cm)"],"data": [[1, 2, 3,4], [4, 5, 6,7]]}'

curl http://127.0.0.1:5000/invocations -H --header 'Content-Type: application/json' --data-raw '{"columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)","petal width (cm)"],"data": [[1, 2, 3,4], [4, 5, 6,7]]}'

"""