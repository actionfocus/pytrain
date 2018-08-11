# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:54:17 2018

@author: actionfocus

mySQL DB connection
"""

import pymysql

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()