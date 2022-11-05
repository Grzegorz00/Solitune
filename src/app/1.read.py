import pandas as pd

# Read data
df = pd.read_csv('../data/employee_init.csv')

# Save the data
df.to_csv('../data/employee_train.csv', index=False)