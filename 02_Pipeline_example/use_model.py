import pickle

import numpy as np

local_pipeline = pickle.load(open('pipeline.pickle','rb'))

# sample predictions
new_prediction = local_pipeline.predict(np.array([[50, 20000]]))
new_prediction_proba = local_pipeline.predict_proba(np.array([[50, 20000]]))

print(new_prediction,new_prediction_proba)