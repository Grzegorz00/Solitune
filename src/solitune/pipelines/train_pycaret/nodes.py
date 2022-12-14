"""
This is a boilerplate pipeline 'train_pycaret'
generated using Kedro 0.18.3
"""

"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.3
"""
import os
import optuna
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler
from pycaret.classification import *

import joblib
import logging

def prepare_data_for_modeling(df):
    '''Prepare data for modeling
    
    Inputs:
    df: a pandas dataframe with employees data
        
    Outputs:
    df: a pandas dataframe with employees data ready for modeling
        X: a pandas dataframe with employees features
        y: a pandas series with employees labels, encoded as integers (0 = not leave, 1 = leave)

    '''
    # Suppress "a copy of slice from a DataFrame is being made" warning
    pd.options.mode.chained_assignment = None
    
    # prepare dataset for classification
    features = df.columns[1:-1]
    X = df[features]
    y = df['LeaveOrNot']

    # identify numeric features in X
    numeric_features = X.select_dtypes(include=[np.number]).columns
    # identify categorical features in X
    categorical_features = X.select_dtypes(exclude=[np.number]).columns

    # Normalize numeric features with MinMaxScaler
    scaler = MinMaxScaler()
    X[numeric_features] = scaler.fit_transform(X[numeric_features])

    # One-hot encode categorical features
    X = pd.get_dummies(X, columns=categorical_features)
    
    #create a dataframe with the features and the labels
    data_prepared = pd.concat([X, y], axis=1)
    return data_prepared

def split_data(df):
    """Splits data into features and targets training and test sets.

    Inputs:
        df: Data containing features and target.

    Output:
        Splited data.
    """
    # split dataset into train and test

    features = df.columns[:-1]
    X = df[features]
    y = df['LeaveOrNot']
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=55)
    
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):    
    '''Train a model predicting if employees will leave or not from features and labels
    
    Inputs:
    X_train: a pandas dataframe with employees features
    y_train: a pandas series with employees labels
        
    Outputs:
    model: a trained model
    
    '''
    data = pd.concat([X_train, y_train], axis=1)
    model_setup = setup(data=data, target='LeaveOrNot')
    best_model = compare_models(sort='AUC', n_select = 1)
    return best_model

def evaluate_model(model, X_test, y_test):
    '''Evaluate a model predicting if employees will leave or not from features and labels
    
    Inputs:
    model: a trained model
    X_test: a pandas dataframe with employees features

        
    Outputs:
    None
    
    '''
    
    labels = y_test.unique()
    y_pred = model.predict(X_test)
    
    # evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy: %.3f' % accuracy)

    #printout the results
    logger = logging.getLogger(__name__)
    logger.info("Model has an accuracy of %.3f on test data.", accuracy)




   
    