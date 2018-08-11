# -*- coding: utf-8 -*-
"""
Created on Sun May 20 11:43:56 2018
@author: actionfocus

说明：本程序只能用于回测，可以通过改动targetDate的值来选择回测日期，但是不可以
        用于交易时间的实时监控

Modifed on Jun.10th:
1.增加写入早上涨幅的逻辑
2.调整历史价格的数据获取函数ts.get_k_data

Modifed on Jun.15th:
1. 更改历史数据的格式，增加前一交易日的收盘价
2. 增加获取前一交易日的收盘价获取逻辑，并加入到最终的输出文件'pre_close'列
3. 修改回测日收盘价的取数逻辑
4. 增加手动设置目标回测日期之前的交易日，手动更新变量previousDate
5. 处置前一交易日处在停牌状态的特殊情形个股，不纳入本回测的计算范围
"""

import openpyxl as pyxl
#import requests
#import re
import pandas as pd
import tushare as ts

targetDate = '2018-06-15' #可以根据选择的回测日期进行调整，格式要符合要求YYYY-MM-DD
previousDate = '2018-06-14' #手工指定目标回测日期的前一个交易日
price_lowerLimit = 4.99 #筛选股价高于这个值
price_upperLimit =  3000 #筛选股价低于这个值
range_item_number = 3586 #目前需要根据行数来手动设置3586,Excel行数-2

codelist=[] 
workBook = pyxl.load_workbook('C:/Temp/full2.xlsx')
sheet1 = workBook.get_sheet_by_name('Sheet1')

for r in range(range_item_number): #目前需要根据行数来手动设置3586,Excel行数-2
   code=sheet1.cell(row=r+2,column=2)
   codelist.append(str(code.value))

mkt_code=[]

count = 1

#stockFull = ts.get_k_data('600001',start='2018-06-08',end='2018-06-08')
#stockFull.drop(stockFull.index,inplace=True)
hist_data_item = {'date':'','open':'','close':'',\
                          'high':'','low':'','volume':'',\
                          'code':'','pre_close':''}
hist_data = pd.DataFrame(hist_data_item, index=['0'])
#hist_data.drop(hist_data.index,inplace=True)

for code in codelist:
    temp1 = ts.get_k_data(code,start=previousDate,end=previousDate)
    temp2 = ts.get_k_data(code,start=targetDate,end=targetDate)
    temp = temp1.append(temp2)
    if not temp2.empty:  #回测日未停牌，不过无法排除该股上一交易日未停牌
        if not temp1.empty: #排除上一交易日停牌情景，不做做计算，默认所有值为0
            hist_date = temp.iloc[1:2,0:1]
            hist_open = temp.iloc[1:2,1:2]
            hist_close = temp.iloc[1:2,2:3]
            hist_high = temp.iloc[1:2,3:4]
            hist_low = temp.iloc[1:2,4:5]
            hist_volume = temp.iloc[1:2,5:6]
            hist_code = temp.iloc[1:2,6:7]
            hist_pre_close = temp.iloc[0:1,2:3]
            data_item = pd.DataFrame({'date':hist_date,'open':hist_open,'close':hist_close,\
                          'high':hist_high,'low':hist_low,'volume':hist_volume,\
                          'code':hist_code,'pre_close':hist_pre_close},index=[count])
            hist_data = hist_data.append(data_item)
        else:
            data_item = pd.DataFrame({'date':'No Deal in Last Day!','open':'0','close':'0',\
                          'high':'0','low':'0','volume':'0',\
                          'code':code,'pre_close':'0'},index=[count])
            hist_data = hist_data.append(data_item)
    
#    stockFull = stockFull.append(temp)

    print "The item", count,"is processed.\n"
    count = count + 1
    
#print stockFull
#stockFull.to_excel('c:/Temp/history_price.xlsx')

os_path_price = 'c:/Temp/'+targetDate+'_history_price.xlsx'

hist_data.to_excel(os_path_price)

print "----股票历史日历的开盘价格与收盘价格获取完毕！----\n"
print "------------------------------break---------------------------\n"


def get_stock_pool():
    #Get qualified stock lists in the pool
#    try:
#        stockFull = ts.get_today_all()
#    except:
#        stockFull = None
#        stockPool = None
#    #print stockFull
#    if stockFull is not None:
#        stockPool = stockFull[\
#                          (stockFull['open'] != 0) & \
#                          (stockFull['close']>price_lowerLimit) & \
#                          (stockFull['close']<price_upperLimit) ]
    
    if hist_data is not None:
        stockPool = hist_data[\
                          (hist_data['open'] != 0) & \
                          (hist_data['close']>price_lowerLimit) & \
                          (hist_data['close']<price_upperLimit) ]
    
    return stockPool

def get_code(code, pre_close, closePM):

    try:
        src = 'tt'
        df = ts.get_tick_data(code,date=targetDate,pause=0.1,src=src)
        #closePM = df['price'][-1:].values[0]
    except:
        df = None
        ErrFlag = 'Y'
    if df is not None:
        if src == 'sn':
            s = df['time']
            index = s[s=='11:30:00']
            startRow = index.index[0]
            endRow = len(df)
            dfAM = df[startRow:endRow]
            openAM = dfAM['price'][-1:].values[0] #上午开盘价
            closeAM = dfAM['price'][1:2].values[0] #上午收盘价
            
        if src == 'tt':
            dfAM = df[df['time']<='11:31:59']           
            closeAM = dfAM['price'][-1:].values[0] #上午收盘价
            openAM = dfAM['price'][1:2].values[0] #上午开盘价
            
        AM_change = (closeAM-pre_close)/openAM*100
        
        quickReturn = (closePM-closeAM)/closeAM*100
    
        mean = dfAM['price'].mean()
        std = dfAM['price'].std()
        cov = std / mean
    
        cnt = dfAM['price'].count()
        mode = dfAM['price'].mode()[0] #找到序列中的众数
        freq = dfAM['price'].value_counts() #计算各个值出现的次数
        freq_mode = freq[mode] #找到众数值出现的次数统计
        mode_ratio = float(freq_mode) / float(cnt)
    
        dataSet = {'code':code,'cov':cov,'mode_ratio':mode_ratio,\
                   'ErrFlag':'N','closePM':closePM,'closeAM':closeAM,\
                   'quickReturn%':quickReturn,\
                   'pre_close':pre_close, 'AM_change%':AM_change,}
        
        #time.sleep(1)
        
    else:
        
        dataSet = {'code':code,'cov':99,'mode_ratio':0,'ErrFlag':ErrFlag,\
                   'closePM':0,'closeAM':0,'quickReturn%':'N/A',\
                   'pre_close':0,'AM_change%':'N/A'}
    
    return dataSet

stock_filtered = get_stock_pool()

print stock_filtered

os_path = 'c:/Temp/'+targetDate+'_sorted.xlsx'

if stock_filtered is not None:

    i=0
#for code in stock_filtered['code']:
#    print code
#    i=i+1
#print "the number of codes is: ", i
    Output = pd.DataFrame({'code':'','cov':'','mode_ratio':'','ErrFlag':'',\
                           'closePM':'','closeAM':'','quickReturn%':'',\
                           'pre_close':'','AM_change%':''}, index=['0'])

    print "\n Starts to calculate cov and mode: \n"
    for code in stock_filtered['code']:
        temp_df = stock_filtered[(stock_filtered['code']==code)]
        pre_close = temp_df['pre_close'].values[0]
        closePM = temp_df['close'].values[0]
        i=i+1
        print "In processing of the ", i, "item, and stock code is: ", code, "\n"
        rs = get_code(code, pre_close, closePM)
        Output = Output.append(rs,ignore_index=True)

    OutputSorted = Output.sort_values(by=['cov','mode_ratio'], ascending=True)

    OutputSorted.to_excel(os_path)

    print OutputSorted

else:
    
    print "Didn't get source data in success.\n"