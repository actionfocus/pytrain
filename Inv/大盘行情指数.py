# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 00:17:13 2018

@author: actionfocus
"""

import tushare as ts
#import time
import datetime

#todayDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))

todayDateTime = datetime.datetime.now()

todayDate = todayDateTime.strftime('%Y-%m-%d')

print todayDate

#yesterdayDateTime = todayDateTime + datetime.timedelta(days=-2)
#
#yesterdayDate = yesterdayDateTime.strftime('%Y-%m-%d')
#
#print yesterdayDate

tradeDay = ts.trade_cal()

isTradeDay = tradeDay[(tradeDay['calendarDate']==todayDate)]['isOpen'].values[0]

print isTradeDay

count = -1 
while not isTradeDay:
    print 'find previous trade day...'
    previousDateTime = todayDateTime + datetime.timedelta(days=count)
    previousDate = previousDateTime.strftime('%Y-%m-%d')
    isTradeDay = tradeDay[(tradeDay['calendarDate']==previousDate)]['isOpen'].values[0]
    count = count-1
    
print previousDate

if count<-1:
    recDate = previousDate
else:
    recDate = todayDate
    
print recDate

df = ts.get_index()

#print df[(df['code']=='000905')]

print df[(df['code']=='000905')]['close'].values[0] #使用时，该值必须配合recDate一起返回

print df[(df['code']=='000001')]['close'].values[0] #使用时，该值必须配合recDate一起返回
