# coding: utf-8 
"""
Created on Fri Mar 16 22:02:26 2018

@author: 
"""

import tushare as ts
import pandas as pd
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

df = ts.get_k_data('603998',start='2018-06-07',end='2018-06-08')
print df
print '----break----'

if df.empty:
    print "df is empty"
#print df.iloc[0:1,0:1]
    

else:
    hist_date = df.iloc[1:2,0:1]
    print hist_date
    hist_open = df.iloc[1:2,1:2]
    hist_close = df.iloc[1:2,2:3]
    hist_high = df.iloc[1:2,3:4]
    hist_low = df.iloc[1:2,4:5]
    hist_volume = df.iloc[1:2,5:6]
    hist_code = df.iloc[1:2,6:7]
    hist_pre_close = df.iloc[0:1,2:3]
    hist_data = pd.DataFrame({'date':hist_date,'open':hist_open,'close':hist_close,\
                          'high':hist_high,'low':hist_low,'volume':hist_volume,\
                          'code':hist_code,'pre_close':hist_pre_close}, index=['0'])
    

temp = pd.DataFrame({'date':hist_date,'open':hist_open,'close':hist_close,\
                          'high':hist_high,'low':hist_low,'volume':hist_volume,\
                          'code':'600344','pre_close':hist_pre_close}, index=['0'])
temp = temp.append(hist_data)
    
print temp

for code in temp['code']:
    temp_df = temp[(temp['code']==code)]
    print code, '\n'
    print temp_df['pre_close'].values[0]
    print '\n'

#hist_data_item = {'date':df,'cov':99,'mode_ratio':0,'ErrFlag':ErrFlag,\
#                   'closePM':0,'closeAM':0,'quickReturn%':'N/A','AM_change%':'N/A'}
#print df['price'][-1:].values[0]
##print df
#s = df[df['time']<='11:31:59']
#s.to_excel('c:/Temp/603866.xlsx')
##endRow = len(df)
#dfAM = df[startRow:endRow]
#dfAM.to_excel('c:/Temp/603861.xlsx')
#s = df['time']
#index = s[s=='11:30:00']
#startRow = index.index[0]
#endRow = len(df)
##df.to_csv('c:/Temp/000001.csv')
##sortDF = df.sort_values(by='time', axis=0, ascending=True) “按某列值排序DF
#dfAM = df[startRow:endRow]
#print dfAM
#mean = dfAM['price'].mean()
#std = dfAM['price'].std()
#cov = std / mean
#print "平均值=",mean
#print "标准差=",std
#print "变异系数=",cov
#dfAM.to_csv('c:/Temp/test600317.csv')
#
#df = ts.get_k_data('600848',start='2018-06-08',end='2018-06-08')
#df2 = ts.get_k_data('600838',start='2018-06-08',end='2018-06-08')
#df =  df.append(df2)
#print df