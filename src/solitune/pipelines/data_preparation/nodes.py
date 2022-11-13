"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.18.3
"""

from hashlib import new
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import LabelEncoder, StandardScaler

from kedro.pipeline import pipeline, node
from kedro.runner import SequentialRunner
from kedro.io import DataCatalog, MemoryDataSet

def encode_categorical_values(dataset):
    """Encode categorical values: Education, Gender, Ever Benched
    Input:    
    dataset: a pandas dataframe with employee orders    
    Output:    
    employee_encoded: pandas dataframe with encoded categorical values 
    """
    le = LabelEncoder()
    dataset=pd.DataFrame(dataset)

    dataset["Education"] = le.fit_transform(dataset["Education"])
    dataset["Gender"] = le.fit_transform(dataset["Gender"])
    dataset["EverBenched"] = le.fit_transform(dataset["EverBenched"])

    employee_encoded = pd.get_dummies(dataset, drop_first=False)
    return employee_encoded
    
def reorder_dataset(dataset):
    """Reorder dataset for better transparency
    Input:    
    dataset: a pandas dataframe with employee orders    
    Output:    
    employee_reordered: pandas dataframe reorded
    """
    leave_or_not = dataset["LeaveOrNot"]
    dataset = dataset.drop("LeaveOrNot", axis=1)
    dataset.insert(loc=len(dataset.columns), column="LeaveOrNot", value=leave_or_not)

    employee_reordered = dataset.drop(["JoiningYear", "PaymentTier"], axis=1)

    return employee_reordered

def load_data(employee):
    """Load raw data for modeling
    Input:    
    employee: a raw csv with employees data    
    Output:    
    pandas_df: pandas dataframe of employee file
    """
    pandas_df = pd.read_csv(employee)
    return pandas_df
