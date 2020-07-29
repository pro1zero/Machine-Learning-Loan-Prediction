import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree
import sqlite3

#GET INPUT

Name = input('enter your name:')
Gender = input('Enter your gender(M/F):')
Age = int(input('enter your age:'))
Married = input('Married(Y/N):')
Dependents = int(input('Number of dependents:'))
Education = input('Applicant Eduction(Graduate/Under Graduate):')
Self_Employed = input('Self Employed(Y/N):')
ApplicantIncome = int(input('enter your monthly income in $:'))
CoapplicantIncome = int(input('enter your CoapplicantIncome income in $:'))
Loan_amount = int(input('Loan Amount:'))
Loan_Amount_Term = int(input('Loan Amount Term in Months:'))
Credit_History = int(input('enter credit history:'))
Property_Area = input('Property Area(Urban / Semi Urban / Rural):')

#COLLECT DATA

info = {'Name' : [Name],
        'Gender' : [Gender],
        'Age' : [Age],
        'Married' : [Married],
        'Dependents' : [Dependents],
        'Education' : [Education],
        'Self_Employed' : [Self_Employed],
        'ApplicantIncome' : [ApplicantIncome],
        'CoapplicantIncome' : [CoapplicantIncome],
        'LoanAmount' : [Loan_amount],
        'Loan_Amount_Term' : [Loan_Amount_Term],
        'Credit_History' : [Credit_History],
        'Property_Area' : [Property_Area]}

info_df = pd.DataFrame(info)

conn = sqlite3.connect('customer.db')
c = conn.cursor()
conn.execute("INSERT INTO CUST_DATA (NAME,GENDER,AGE,MARRIED,DEPENDENTS,EDUCATION,SELF_EMPLOYED,MONTHLY_INCOME,YEARLY_INCOME,LOAN_AMOUNT,LOAN_AMOUNT_TERM,PROPERTY_AREA) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(Name,Gender,Age,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,Loan_amount,Loan_Amount_Term,Property_Area));
conn.commit()
conn.close()

train = pd.read_csv('train.csv')
test = info_df

train_mod = train
test_mod = test

train_mod['LoanAmount'] = train_mod['LoanAmount'].fillna(train_mod['LoanAmount'].median())
test_mod['LoanAmount'] = test_mod['LoanAmount'].fillna(test_mod['LoanAmount'].median())

train_mod['Credit_History'].fillna(1.0, inplace=True)
test_mod['Credit_History'].fillna(1.0, inplace=True)

train_mod['Gender'].fillna('Male', inplace=True)
test_mod['Gender'].fillna('Male', inplace=True)

train_mod['TotalIncome'] = train_mod['ApplicantIncome'] + train_mod['CoapplicantIncome']
test_mod['TotalIncome'] = test_mod['ApplicantIncome'] + test_mod['CoapplicantIncome']

train_mod['TotalIncome_log'] = np.log(train_mod['TotalIncome'])
test_mod['TotalIncome_log'] = np.log(test_mod['TotalIncome'])

def classification_model(model, train_mod, predictors, outcome):
    global test
    x_train = train_mod[predictors].values
    y_train = train_mod['Loan_Status'].values
    model.fit(x_train,y_train)
    x_test = test[predictors].values
    predictions = model.predict(x_test)
    test_mod['Loan_Status'] = predictions
    stringss = test_mod['Loan_Status']
    if predictions == 'Y':
        print("you can be eligible to get loan, please visit your bank.")
    else:
        print("you are not eligible to get loan.")
        
model = sklearn.tree.DecisionTreeClassifier()
predictors = ['Credit_History','TotalIncome_log','LoanAmount']
outcome = 'Loan_Status'
classification_model(model, train, predictors, outcome)
