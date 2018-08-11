# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:30:36 2018

@author: 
"""
import tushare as ts
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

code = '300033'
try:
    src = 'tt'
    df = ts.get_tick_data(code,date='2018-05-18',pause=0.1,src=src)
except:
    df = None
    ErrFlag = 'Y'

closePM = df['price'][-1:].values[0]
    
if df is not None:
    #df.to_excel('c:/Temp/test.xlsx')
    if src == 'sn':
        s = df['time']
        index = s[s=='11:30:00']
        startRow = index.index[0]
        endRow = len(df)
        dfAM = df[startRow:endRow]          
    if src == 'tt':
        dfAM = df[df['time']<='11:31:59']
        
    closeAM = dfAM['price'][-1:].values[0]
    print closeAM
    mean = dfAM['price'].mean()
    std = dfAM['price'].std()
    cov = std / mean    

    cnt = dfAM['price'].count()
    mode = dfAM['price'].mode()[0] #找到序列中的众数
    freq = dfAM['price'].value_counts() #计算各个值出现的次数
    freq_mode = freq[mode] #找到众数值出现的次数统计
    mode_ratio = float(freq_mode) / float(cnt)
    
    dataSet = {'code':code,'cov':cov,'mode_ratio':mode_ratio,'ErrFlag':'N'}
                
else:
        
    dataSet = {'code':code,'cov':99,'mode_ratio':0,'ErrFlag':ErrFlag}
    
print dataSet