# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:43:56 2018

Modifed on Jun.10th for adding "AM_change logic"

基础股价取腾讯数据源，替代上一版本的新浪数据源

本程序只能抓取腾讯的实时数据，并用腾讯分时数据来实时监控，不可以用来回测

@author: actionfocus
"""

import tushare as ts
import pandas as pd
import openpyxl as pyxl
import requests
import re
#import time
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

targetDate = '2018-06-08' #选择回测日期
price_lowerLimit = 4.99  #用来选择运行程序时候的价格不低于这个最低价
price_upperLimit =  3000 #用来选择运行程序时候的价格不超过这个最高价
range_item_number = 3586 #目前需要根据行数来手动设置3586,Excel行数-2

def get_stock_price(stockcode):
    url1 = 'http://qt.gtimg.cn/q='+stockcode
    result = requests.get(url1)
    line = result.text.rstrip('\n')
    parts = re.split('=',line)
    quotes = re.split('~',parts[1])
    print quotes[3]
    dataSet = {'code':stockcode,'trade':float(quotes[3]),'open':float(quotes[5])}
    return dataSet

codelist=[] 
workBook = pyxl.load_workbook('C:/Temp/full2.xlsx')
sheet1 = workBook.get_sheet_by_name('Sheet1')

for r in range(range_item_number): #目前需要根据行数来手动设置3586,Excel行数-2
   code=sheet1.cell(row=r+2,column=2)
   codelist.append(str(code.value))

mkt_code=[]
instant_price=[]

Output = pd.DataFrame({'code':'','trade':'','open':''}, index=['0'])

count = 0

for code in codelist:
    if code.startswith('6') or code.startswith('9'): #这个判断规则只适用于A股市场的数据源
        mktcode = 'sh'
    else:
        mktcode = 'sz'
    full_stockcode = mktcode+code
    rs = get_stock_price(full_stockcode)
    Output = Output.append(rs,ignore_index=True)
    print full_stockcode, ". The item", count,"is processed.\n"
    count = count + 1

def get_stock_pool():
    #Get qualified stock lists in the pool
    try:
        #stockFull = ts.get_today_all()
        stockFull = Output
    except:
        stockFull = None
        stockPool = None
    #print stockFull
    if stockFull is not None:
        stockPool = stockFull[\
                          (stockFull['open'] != 0) & \
                          (stockFull['trade']>price_lowerLimit) & \
                          (stockFull['trade']<price_upperLimit) ]
    return stockPool

def get_code(code):
    try:
        src = 'tt'
#        df = ts.get_tick_data(code,date=targetDate,pause=0.1,src=src)
#改程序下面需要更新为取腾讯的分时数据        
#        closePM = df['price'][-1:].values[0]
#    except:
#        df = None
#        ErrFlag = 'Y'
#    if df is not None:
#        if src == 'sn':
#            s = df['time']
#            index = s[s=='11:30:00']
#            startRow = index.index[0]
#            endRow = len(df)
#            dfAM = df[startRow:endRow]
#            openAM = dfAM['price'][-1:].values[0] #上午开盘价
#            closeAM = dfAM['price'][1:2].values[0] #上午收盘价
#            
#        if src == 'tt':
#            dfAM = df[df['time']<='11:31:59']           
#            closeAM = dfAM['price'][-1:].values[0] #上午收盘价
#            openAM = dfAM['price'][1:2].values[0] #上午开盘价
#            
#        AM_change = (closeAM-openAM)/openAM*100
#        
#        quickReturn = (closePM-closeAM)/closeAM*100
#    
#        mean = dfAM['price'].mean()
#        std = dfAM['price'].std()
#        cov = std / mean
#    
#        cnt = dfAM['price'].count()
#        mode = dfAM['price'].mode()[0] #找到序列中的众数
#        freq = dfAM['price'].value_counts() #计算各个值出现的次数
#        freq_mode = freq[mode] #找到众数值出现的次数统计
#        mode_ratio = float(freq_mode) / float(cnt)
#    
#        dataSet = {'code':code,'cov':cov,'mode_ratio':mode_ratio,\
#                   'ErrFlag':'N','closePM':closePM,'closeAM':closeAM,\
#                   'quickReturn%':quickReturn,'AM_change%':AM_change}
#        
#        #time.sleep(1)
#        
#    else:
#        
#        dataSet = {'code':code,'cov':99,'mode_ratio':0,'ErrFlag':ErrFlag,\
#                   'closePM':0,'closeAM':0,'quickReturn%':'N/A','AM_change%':'N/A'}
#    
#    return dataSet
#
#stock_filtered = get_stock_pool()
#
#os_path = 'c:/Temp/'+targetDate+'_sorted.xlsx'
#
#if stock_filtered is not None:
#
#    i=0
##for code in stock_filtered['code']:
##    print code
##    i=i+1
##print "the number of codes is: ", i
#    Output = pd.DataFrame({'code':'','cov':'','mode_ratio':'','ErrFlag':'',\
#                           'closePM':'','closeAM':'','quickReturn%':'','AM_change%':''}, index=['0'])
#
#    print "\n Starts to calculate cov and mode: \n"
#    for code in stock_filtered['code']:
#        i=i+1
#        print "In processing of the ", i, "item, and stock code is: ", code, "\n"
#        rs = get_code(code)
#        Output = Output.append(rs,ignore_index=True)
#
#    OutputSorted = Output.sort_values(by=['cov','mode_ratio'], ascending=True)
#
#    OutputSorted.to_excel(os_path)
#
#    print OutputSorted
#
#else:
#    
#    print "Didn't get source data in success.\n"