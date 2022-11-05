import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, r2_score
from datetime import date, datetime

# Load model
model = pickle.load(open("model/model_1.0.pkl", 'rb'))

# Read test data
test_data = pd.read_csv("../data/employee_test.csv")

X = test_data['x'].values.reshape(-1,1)
y = test_data['y'].values.reshape(-1,1)

# Predict
predictions = model.predict(X)

# Evaluate
RMSE = np.sqrt(mean_squared_error(y, predictions))
r2 = r2_score(y, predictions)
print('RMSE on test data: ', RMSE)
print('r2 on test data: ', r2)