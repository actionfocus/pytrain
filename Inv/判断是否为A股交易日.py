# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:08:48 2018

@author: actionfocus
"""

#用于判断一个给定的日期是否是交易日

import tushare as ts
df = ts.trade_cal()

print df[(df['calendarDate']=='2018-06-15')]
print df[(df['calendarDate']=='2018-06-15')]['isOpen'].values[0]