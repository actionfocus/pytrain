# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 13:49:27 2018

@author: actionfocus

依据intexchg的值，对inexcalc进行计算和更新操作
"""


import pymysql
import pandas as pd

# Open database connection
db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to select a record from the table.

sql = "SELECT * FROM intexchg"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
#创建dataframe的结构，无记录
   intexchgDF = pd.DataFrame(columns=['recDate', 'Interest', 'Exchange', 'shIndex','cnIndex','ratio'])
   count = 1
   for row in results:
      #print (row)
      recDate = row[0]
      Interest = float(row[1])
      Exchange = float(row[2])
      shIndex = float(row[3])
      cnIndex = float(row[4])
      ratio = float(Interest/Exchange)
      # Now print fetched result
#      print ("date = %s Interest = %f,Exchange = %f,shIndex = %f,cnIndex = %f" % \
#             (recDate, Interest, Exchange, shIndex, cnIndex))
      #print recDate, Interest, Exchange, shIndex, cnIndex
      tmpDF = pd.DataFrame({'recDate':recDate,'Interest':Interest,'Exchange':Exchange,\
                          'shIndex':shIndex,'cnIndex':cnIndex,'ratio':ratio},index=[count])
      intexchgDF = intexchgDF.append(tmpDF)
      count = count+1
    
   #print intexchgDF
      
except:
   import traceback
   traceback.print_exc()

   print ("Error: unable to fetch data")


#print intexchgDF['ratio'][0:24]
rows = len(intexchgDF)
index = 0
while index<=rows-1:
#    print intexchgDF.iloc[index]['shIndex']
#    print '\n'
    recDate = intexchgDF.iloc[index]['recDate']
    Interest = intexchgDF.iloc[index]['Interest']
    Exchange = intexchgDF.iloc[index]['Exchange']
    shIndex = intexchgDF.iloc[index]['shIndex']
    cnIndex = intexchgDF.iloc[index]['cnIndex']
    ratio = intexchgDF.iloc[index]['ratio']
    cnIndexAdj = cnIndex/1.90
    InterestAdj = 11000/Interest
    ExchangeAdj = 25/Exchange
    calcFigure1 = 38/(Interest+Exchange)
    if (index-24)>=0:
        start=index-24
        end=index+1
        tmpInt = intexchgDF['Interest'][start:end]
#        std = tmpInt.std()
        mean = tmpInt.mean()
#        Interest_cov = 10000*std/mean
        final=0.0
        for item in tmpInt:
            tmp=item-mean
            rs=tmp*tmp
            final=final+rs
        Interest_cov = 10000*final/mean
        if index==24:
            print 'Interest_cov=',Interest_cov,'\n'
            print tmpInt
        tmpEx = intexchgDF['Exchange'][start:end]
#        std = tmpEx.std()
        mean = tmpEx.mean()
#        Exchange_cov = 10000*std/mean
        final=0.0
        for item in tmpEx:
            tmp=item-mean
            rs=tmp*tmp
            final=final+rs
        Exchange_cov = 10000*final/mean
        tmpRa = intexchgDF['ratio'][start:end]
#        std = tmpRa.std()
        mean = tmpRa.mean()
#        ratio_cov = 10000*std/mean
        final=0.0
        for item in tmpRa:
            tmp=item-mean
            rs=tmp*tmp
            final=final+rs
        ratio_cov = 10000*final/mean
        if Exchange_cov > ratio_cov:
            decision1 = 'Exchange'
        else:
            decision1 = 'Interest'
        print Interest, Exchange, shIndex, cnIndex, ratio, cnIndexAdj, InterestAdj,\
            ExchangeAdj, calcFigure1, Interest_cov, Exchange_cov, ratio_cov, decision1,\
            'row=',index+1,'\n'
        #数据更新到表inexcalc
        sql = """INSERT INTO inexcalc(recDate,Interest, Exchange, shIndex, cnIndex,
         ratio, cnIndexAdj, InterestAdj, ExchangeAdj, calcFigure1, Interest_cov,
         Exchange_cov, ratio_cov, decision1) 
         VALUES ('%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,'%s')"""
        data = (recDate,Interest, Exchange, shIndex, cnIndex, ratio, cnIndexAdj,\
            InterestAdj, ExchangeAdj, calcFigure1, Interest_cov,\
            Exchange_cov, ratio_cov, decision1)
    else:
        print Interest, Exchange, shIndex, cnIndex, ratio, cnIndexAdj, InterestAdj,\
            ExchangeAdj, calcFigure1,'row=',index+1,'\n'
        #数据更新到表inexcalc
        sql = """INSERT INTO inexcalc(recDate,Interest, Exchange, shIndex, cnIndex,
         ratio, cnIndexAdj, InterestAdj, ExchangeAdj, calcFigure1) 
         VALUES ('%s',%f,%f,%f,%f,%f,%f,%f,%f,%f)"""
        data = (recDate,Interest, Exchange, shIndex, cnIndex, ratio, cnIndexAdj,\
            InterestAdj, ExchangeAdj, calcFigure1)
    try:
        # Execute the SQL command
        cursor.execute(sql % data)
        # Commit your changes in the database
        db.commit()   
    except:
            # Rollback in case there is any error
            db.rollback()
            print "inexcalc update error"
    index=index+1
    

# disconnect from server
db.close()