# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:03:36 2018

@author: actionfocus

基于csv文件的数据库初始化案例

table - intexchg批量上载
"""

import pymysql

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to upload records into the database. 注意下面SQL语句中盘符文件的"/",windows下也不能用"\"
sql = """LOAD DATA INFILE 'C:/mysql/initData/testdata.csv' 
        INTO TABLE intexchg 
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   flag = 1
except:
   # Rollback in case there is any error
   db.rollback()
   flag = 0

if flag == 0:
    print 'Upload failed.'
else:
    print('Yes, Insert Successfull.')

# disconnect from server
db.close()

