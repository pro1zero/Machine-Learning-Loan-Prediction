import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.execute("SELECT NAME,GENDER,AGE,MARRIED,DEPENDENTS,EDUCATION,SELF_EMPLOYED,MONTHLY_INCOME,YEARLY_INCOME,LOAN_AMOUNT,LOAN_AMOUNT_TERM,PROPERTY_AREA from CUST_DATA")
for data in cursor:
    print("name=",data[0])
    print("gender=",data[1])
    print("age=",data[2])
    print("married=",data[3])
    print("dependents=",data[4])
    print("education=",data[5])
    print("self_employed=",data[6])
    print("monthly_income=",data[7])
    print("yearly_income=",data[8])
    print("loan_amount=",data[9])
    print("loan_amount_term=",data[10])
    print("property_area=",data[11])


conn.close()
