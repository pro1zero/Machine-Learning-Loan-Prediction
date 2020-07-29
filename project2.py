import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree


train = pd.read_csv('data2.csv')
test = pd.read_csv('data.csv')

train_mod = train
test_mod = test



def classification_model(model, train_mod, predictors, outcome):
    global test
    x_train = train_mod[predictors].values
    y_train = train_mod['person'].values
    model.fit(x_train,y_train)
    x_test = test[predictors].values
    predictions = model.predict(x_test)
    test_mod['person'] = predictions
    stringss = test_mod['person']
        
model = sklearn.tree.DecisionTreeClassifier()
predictors = ['time']
outcome = 'person'
classification_model(model, train, predictors, outcome)
