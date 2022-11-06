import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import warnings
warnings.filterwarnings('ignore')


def prepare_data_for_modeling(dataset):
    '''Prepare data for modeling
    
    Inputs:
    df: a pandas dataframe with customers data
        
    Outputs:
    df: a pandas dataframe with customers data ready for modeling
        X: a pandas dataframe with customer features
        y: a pandas series with customer labels, encoded as integers (0 = low revenue, 1 = high revenue)

    '''

    #Encoding categorical value
    le = LabelEncoder()

    dataset['Education']=le.fit_transform(dataset['Education'])
    dataset['Gender']=le.fit_transform(dataset['Gender'])
    dataset['EverBenched']=le.fit_transform(dataset['EverBenched'])

    dataset = pd.get_dummies(dataset, drop_first=False)

    #Dataset Reordering
    leave_or_not = dataset['LeaveOrNot']
    dataset = dataset.drop('LeaveOrNot', axis=1)
    dataset.insert(loc=len(dataset.columns), column='LeaveOrNot', value=leave_or_not)
    
    dataset = dataset.drop(['JoiningYear', 'PaymentTier'], axis=1)

    return dataset

def train(dataset):    
    '''Train a model predicting high-revenue customers from features and labels
    
    Inputs:
    df: a pandas dataframe with customers data
        
    Outputs:
    model: a trained model
    
    '''
    #transforming dataset to array
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    #separating training set and test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=27)

    #scaling the training set
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    #Model Building and Training with the Training Set
    classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=27)
    classifier.fit(x_train, y_train)

    #Predicting the Test Set Result
    y_pred = classifier.predict(x_test)
    result_np = np.concatenate((y_pred.reshape(len(y_pred), 1), (y_test.reshape(len(y_test), 1))), 1)
    result = pd.DataFrame(result_np, columns=['Prediction', 'Real_Value'])
    print(result)

    #Accuracy report
    print(classification_report(y_test, y_pred))

    #Accuracy Report with K-Fold Cross Validation
    val_score = cross_val_score(estimator=classifier, X = x_train, y=y_train, cv=10)
    print("Accuracy: {:.2f} %".format(val_score.mean()*100))
    print("Std. Dev: {:.2f} %".format(val_score.std()*100))

    
    return classifier

# Read customers_labeled dataset

df = pd.read_csv('src/app/test.csv') #data/03_prepared/data.csv

data_prepared = prepare_data_for_modeling(df)
# Train the model
model = train(data_prepared)


