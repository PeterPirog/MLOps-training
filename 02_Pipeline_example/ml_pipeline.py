import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.pipeline import Pipeline

training_data = pd.read_csv('storepurchasedata_large.csv')

training_data.describe()

X = training_data.iloc[:, :-1].values
y = training_data.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=0)

# Prepare pipeline
sc = StandardScaler()
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

pipe=Pipeline([('scaler',sc),
               ('classifier',classifier)])


# Model training
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)
y_prob = pipe.predict_proba(X_test)[:, 1]

# calculate results
cm = confusion_matrix(y_test, y_pred)

print(accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

# sample predictions
new_prediction = pipe.predict(np.array([[50, 20000]]))
new_prediction_proba = pipe.predict_proba(np.array([[50, 20000]]))

print(new_prediction,new_prediction_proba)

# Picking the Pipeline


model_file = "pipeline.pickle"

pickle.dump(pipe, open(model_file, 'wb'))

