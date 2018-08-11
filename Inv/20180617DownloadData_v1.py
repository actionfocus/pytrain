# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:21:34 2018

@author: actionfocus
"""
import pymysql
import openpyxl as pyxl

wb = pyxl.Workbook()
sheet = wb.get_active_sheet()
sheet.title='inexcalc'

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

dataSet=['recDate','Interest','Exchange','shIndex','cnIndex','ratio','cnIndexAdj',\
         'InterestAdj','ExchangeAdj','calcFigure1','interest_cov','exchange_cov',\
         'ratio_cov','decision1']
sheet.append(dataSet)

sql = "SELECT * FROM inexcalc"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
#   print type(results)

   #intexchgDF = pd.DataFrame(columns=['reDate', 'Interest', 'Exchange', 'shIndex','cnIndex'])
   count = 1
   for row in results:
      dataSet=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],\
               row[9],row[10],row[11],row[12],row[13]]
      sheet.append(dataSet)
      count = count+1 
except:
   import traceback
   traceback.print_exc()

   print ("Error: unable to fetch data")

# disconnect from server
db.close()

try:
    wb.save('C:/Temp/inexcalc.xlsx')
    print 'Spreadsheet saved.'
except:
    print 'Save failed.'