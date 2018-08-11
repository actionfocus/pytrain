# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:44:33 2018

@author: 
"""
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import openpyxl as pyxl
import requests
import re
import pandas as pd
import tushare as ts

def get_stock_price(stockcode):
    url1 = 'http://qt.gtimg.cn/q='+stockcode
    result = requests.get(url1)
    line = result.text.rstrip('\n')
    parts = re.split('=',line)
    quotes = re.split('~',parts[1])
    print quotes[3]
    dataSet = {'code':stockcode,'latest_price':float(quotes[3]),'open_price':float(quotes[5])}
    return dataSet

codelist=[] 
workBook = pyxl.load_workbook('C:/Temp/full2.xlsx')
sheet1 = workBook.get_sheet_by_name('Sheet1')

for r in range(4): #目前需要根据行数来手动设置3586,Excel行数-2
   code=sheet1.cell(row=r+2,column=2)
   codelist.append(str(code.value))

mkt_code=[]
instant_price=[]

Output = pd.DataFrame({'code':'','latest_price':'','open_price':''}, index=['0'])

count = 0

stockFull = ts.get_k_data('600001',start='2018-06-08',end='2018-06-08')
stockFull.drop(stockFull.index,inplace=True)

for code in codelist:
    temp = ts.get_k_data(code,start='2018-06-08',end='2018-06-08')
    
    stockFull = stockFull.append(temp)
    if code.startswith('6') or code.startswith('9'): #这个判断规则只适用于A股市场的数据源
        mktcode = 'sh'
    else:
        mktcode = 'sz'
    full_stockcode = mktcode+code
    rs = get_stock_price(full_stockcode)
    Output = Output.append(rs,ignore_index=True)
    print full_stockcode, ". The item", count,"is processed.\n"
    count = count + 1
    
#print Output[Output['open_price']>0]
#Output.to_excel('c:/Temp/fullprice.xlsx')
print stockFull