# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:55:50 2018

@author: 
"""

import tushare as ts

df = ts.get_tick_data('300055',date='2018-06-08',src='tt')
s = df['time']
print s
s.to_excel('c:/Temp/test.xlsx')
#index = s[s=='11:30:00'] #这个判断方法只适用于SINA数据源
#startRow = index.index[0]
#endRow = len(df)
#dfAM = df[startRow:endRow]
#print dfAM
#print '----break1---'
#print dfAM['price']
#print '----break2---'
print dfAM['price'][-1:].values[0]#上午收盘价 tt数据源
#print '----break3---'
#print dfAM['price'][1:2].values[0] #上午收盘价 tt数据源

#cnt = dfAM['price'].count()
#mode = dfAM['price'].mode()[0] #找到序列中的众数
#freq = dfAM['price'].value_counts() #计算各个值出现的次数
#freq_mode = freq[mode] #找到众数值出现的次数统计
#print "总个数=", cnt
#print "众数=", mode
#print "众数出现次数=", freq_mode
#mode_ratio = float(freq_mode) / float(cnt)
#print "众数出现的比率=", mode_ratio