import sqlite3

conn = sqlite3.connect('customer.db')

conn.execute('''CREATE TABLE IF NOT EXISTS CUST_DATA 
            (NAME INT NOT NULL,
            GENDER TEXT NOT NULL,
            AGE INT NOT NULL,
            MARRIED TEXT NOT NULL,
            DEPENDENTS INT NOT NULL,
            EDUCATION TEXT NOT NULL,
            SELF_EMPLOYED TEXT NOT NULL,
            MONTHLY_INCOME INT NOT NULL,
            YEARLY_INCOME INT NOT NULL,
            LOAN_AMOUNT INT NOT NULL,
            LOAN_AMOUNT_TERM INT NOT NULL,
            PROPERTY_AREA TEXT NOT NULL);''')
print("Table Created.")

conn.close()
