# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:18:25 2018

@author:
"""

import tushare as ts
import datetime as dt

N=60
stockcode = 'sh600820'

today = dt.date.today()
Ndays = today - dt.timedelta(days=N)
print "start date:", Ndays, "\t", "end date:", today

df = ts.get_hist_data(stockcode, start=str(Ndays), end=str(today))

#print df

max = df['high'].max()
min = df['low'].min()
print "max:", max, "\t", "min:", min
currentPrice = df['close'][0]
print "currentPrice:",currentPrice
position = (currentPrice-min) / (max-min) * 100
costFactor = 0.01
absoluteRaise = (max-currentPrice)/currentPrice *(1-costFactor) * 100

print "position:", position
print "absoluteRaise in potential:", absoluteRaise

if position < 10:
    print "Good to buy in short time"
elif position < 25:
    print "Consider to buy in short time."
elif position < 45:
    print "Validate with other factors to make decision in short time."
else:
    print "Not good to buy in short time."