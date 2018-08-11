# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 21:30:33 2018

@author: actionfocus
"""

#根据主力资金净流入比率，全部资金净流入比率，结合股票涨跌幅来挑选股票

#import tushare as ts
import pandas as pd
import datetime
import time
import thread
import openpyxl as pyxl
import requests
import re


codelist=[]
 
workBook = pyxl.load_workbook('C:/laptop/00Python/HKList.xlsx')
    
sheet1 = workBook.get_sheet_by_name('Sheet1')

for r in range(171): #目前需要根据行数来手动设置
    code=sheet1.cell(row=r+2,column=2)
    codelist.append(str(code.value))

#stockcode='sz002230'

def get_money_data(stockcode):
    url1 = 'http://qt.gtimg.cn/q='+stockcode
    result = requests.get(url1)
    line = result.text.rstrip('\n')
    parts = re.split('=',line)
    quotes = re.split('~',parts[1])
    stockID = quotes[2]
    stockName = quotes[1]
    PE = quotes[39]
    liutongshizhi = float(quotes[44])
    zongshizhi =  float(quotes[45]) 
    liutongRatio = liutongshizhi / zongshizhi * 100
    url2 = 'http://qt.gtimg.cn/q=ff_'+stockcode
    ff_result = requests.get(url2)
    line1 = ff_result.text.rstrip('\n')
    seg1 = re.split('=',line1)
    ff = re.split('~',seg1[1])
    if ff[0] <> '1;':
        zhuliNet = float(ff[3])
        sanhuNet = float(ff[7])
        #主力净流入占流通市值的比率
        zhuliRatio = zhuliNet / (liutongshizhi*10000) * 100
        print stockID, '\t', stockName, '\t', zhuliNet, '\t', zhuliRatio
        data = {'name':stockName,'zhuliRatio':zhuliRatio,'code':stockID, 'liutongRatio':liutongRatio}
        return data
    else:
        print stockID, '\t', stockName, '\t', 'N/A', '\t', 'N/A'
        return {'name':stockName,'zhuliRatio':0,'code':stockID, 'liutongRatio':0}

df = pd.DataFrame({'name':'','zhuliRatio':'','code':'','liutongRatio':''}, index=['0'])
    
for code in codelist:
    #print code[2:4]
    if code[:2] <> 'hk' and code[2:4] <> '51' and code[2:4] <>'15':
        rs = get_money_data(code)
        df = df.append(rs,ignore_index=True)
print df.sort_values(by='zhuliRatio', ascending=False)
