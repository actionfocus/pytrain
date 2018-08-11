# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:38:21 2018

@author: actionfocus
"""

import pymysql

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO intexchg(recDate,
   Interest, Exchange, shIndex, cnIndex)
   VALUES ('2017-01-03', 3.060, 6.9595, 3135.92, 6320.76)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

## 再次插入一条记录
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO intexchg(recDate,
   Interest, Exchange, shIndex, cnIndex)
   VALUES ('2017-01-04', 3.146, 6.8699, 3158.79, 6394.67)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
print (sql)
print('Yes, Insert Successfull.')

# disconnect from server
db.close()