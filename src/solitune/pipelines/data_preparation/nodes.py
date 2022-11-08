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

def prepare_data_for_modeling(dataset):
    """
    Document prepare data function
    """

    # Encoding categorical value
    le = LabelEncoder()

    dataset["Education"] = le.fit_transform(dataset["Education"])
    dataset["Gender"] = le.fit_transform(dataset["Gender"])
    dataset["EverBenched"] = le.fit_transform(dataset["EverBenched"])

    dataset = pd.get_dummies(dataset, drop_first=False)

    # Dataset Reordering
    leave_or_not = dataset["LeaveOrNot"]
    dataset = dataset.drop("LeaveOrNot", axis=1)
    dataset.insert(loc=len(dataset.columns), column="LeaveOrNot", value=leave_or_not)

    dataset = dataset.drop(["JoiningYear", "PaymentTier"], axis=1)

    return dataset

def load_data():
    # Load data
    df = pd.read_csv("../../data/01_raw/employee.csv")
    return prepare_data_for_modeling(df)
