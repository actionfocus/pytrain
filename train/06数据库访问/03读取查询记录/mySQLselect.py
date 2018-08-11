# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 20:50:22 2018

@author: actionfoucs
"""

import pymysql
import pandas as pd

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to select a record from the table.
#sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > %d" % (1000)

sql = "SELECT * FROM intexchg"
#print (sql)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
#   print type(results)
   print "---------------\n"
   intexchgDF = pd.DataFrame(columns=['reDate', 'Interest', 'Exchange', 'shIndex','cnIndex'])
   count = 1
   for row in results:
      #print (row)
      recDate = row[0]
      Interest = row[1]
      Exchange = row[2]
      shIndex = row[3]
      cnIndex = row[4]
      # Now print fetched result
#      print ("date = %s Interest = %f,Exchange = %f,shIndex = %f,cnIndex = %f" % \
#             (recDate, Interest, Exchange, shIndex, cnIndex))
      #print recDate, Interest, Exchange, shIndex, cnIndex
      tmpDF = pd.DataFrame({'reDate':recDate,'Interest':Interest,'Exchange':Exchange,\
                          'shIndex':shIndex,'cnIndex':cnIndex},index=[count])
      intexchgDF = intexchgDF.append(tmpDF)
      count = count+1
    
   print intexchgDF
      
except:
   import traceback
   traceback.print_exc()

   print ("Error: unable to fetch data")

# disconnect from server
db.close()