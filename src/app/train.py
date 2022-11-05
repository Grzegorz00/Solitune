import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import metrics

from sklearn.preprocessing import MinMaxScaler

def prepare_data_for_modeling(df):
    '''Prepare data for modeling
    
    Inputs:
    df: a pandas dataframe with customers data
        
    Outputs:
    df: a pandas dataframe with customers data ready for modeling
        X: a pandas dataframe with customer features
        y: a pandas series with customer labels, encoded as integers (0 = low revenue, 1 = high revenue)

    '''
    # Suppress "a copy of slice from a DataFrame is being made" warning
    pd.options.mode.chained_assignment = None
    
    # prepare dataset for classification
    features = df.columns[:-1]
    X = df[features]
    y = df['high_revenue']

    # identify numeric features in X
    numeric_features = X.select_dtypes(include=[np.number]).columns
    # identify categorical features in X
    categorical_features = X.select_dtypes(exclude=[np.number]).columns

    # Normalize numeric features with MinMaxScaler
    scaler = MinMaxScaler()
    X[numeric_features] = scaler.fit_transform(X[numeric_features])

    # One-hot encode categorical features
    X = pd.get_dummies(X, columns=categorical_features)

    # transform bool in y to 0/1
    y = y.astype(int)
    
    #create a dataframe with the features and the labels
    data_prepared = pd.concat([X, y], axis=1)
    return data_prepared

def train(df):    
    '''Train a model predicting high-revenue customers from features and labels
    
    Inputs:
    df: a pandas dataframe with customers data
        
    Outputs:
    model: a trained model
    
    '''
    
    # Suppress "a copy of slice from a DataFrame is being made" warning
    pd.options.mode.chained_assignment = None
    
    features = df.columns[:-1]
    X = df[features]
    y = df['high_revenue']
    
    # split dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # train the model
    #model = DecisionTreeClassifier()
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # test the model
    y_pred = model.predict(X_test)

    # evaluate the model
    
    #print(accuracy_score(y_test, y_pred))
    print(metrics.classification_report(y_test, y_pred))
    
    return model

# Read customers_labeled dataset

df = pd.read_csv('data/03_prepared/customers_labeled.csv')

data_prepared = prepare_data_for_modeling(df)
# Train the model
model = train(data_prepared)
