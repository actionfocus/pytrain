# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:38:20 2018

@author: 
"""

#下载最新收盘价格到Excel中

import requests
import openpyxl as pyxl
import pandas as pd
import re
    
def get_price(stockcode):
    url1 = 'http://qt.gtimg.cn/q='+stockcode
    result = requests.get(url1)
    line = result.text.rstrip('\n')
    parts = re.split('=',line)
    quotes = re.split('~',parts[1])
    #print quotes
    return quotes[3]

def get_codelist():
    codelist = []
    workBook = pyxl.load_workbook('C:/laptop/00Python/HKList.xlsx')
    sheet1 = workBook.get_sheet_by_name('Sheet1')
    for r in range(170): #目前需要根据行数来手动设置
        code=sheet1.cell(row=r+2,column=2)
        codelist.append(str(code.value))
    return codelist

StockCodeList = get_codelist()
#print StockCodeList[0][2:]   
df = pd.DataFrame({'stockcode':'','closePrice':''}, index=['0'])
for code in StockCodeList:
    closePrice = get_price(code)
    item = {'stockcode':code,'closePrice':closePrice}
    df = df.append(item,ignore_index=True)

df.to_excel('C:/laptop/PC/tracking list/UpdatePrice.xlsx')

print "Done."
    