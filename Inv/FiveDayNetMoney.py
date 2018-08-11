# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:21:33 2018

@author: 
"""
#获取个股5个交易日的主力净流入信息

import re
import pandas as pd
import requests

stockcode = 'sh600820'

ff_url = 'http://qt.gtimg.cn/q=ff_'+stockcode

ff_result = requests.get(ff_url)
line1 = ff_result.text.rstrip('";\n')
seg1 = re.split('=',line1)
seg1[1]=seg1[1].lstrip('"')
ff = re.split('~',seg1[1])
#print ff[0], ff[13], ff[1], ff[2], ff[14], ff[15], ff[16], ff[17]

df = pd.DataFrame({'name':'','date':'','code':'','in':'','out':'','net':''}, index=['0'])

netamount = float(ff[1])-float(ff[2])

item = {'name':ff[12],'date':ff[13],'code':ff[0],'in':ff[1],'out':ff[2],'net':netamount}

df = df.append(item,ignore_index=True)

for i in range(4):
    index = i+14
    dayNet = ff[index].split('^')
    #print dayNet
    netamount = float(dayNet[1])-float(dayNet[2])
    item = {'name':ff[12],'date':dayNet[0],'code':ff[0],'in':float(dayNet[1]),'out':float(dayNet[2]),'net':netamount}
    df = df.append(item,ignore_index=True)

print df
FiveDaySum = 0
TwoDaySum = 0
ThreeDaySum = 0

for elem in df['net'][1:3]:
    TwoDaySum = TwoDaySum + elem

for elem in df['net'][1:4]:
    ThreeDaySum = ThreeDaySum + elem
    
for elem in df['net'][1:6]:
    FiveDaySum = FiveDaySum + elem

print "2days: ", TwoDaySum
print "3days: ", ThreeDaySum
print "5days: ", FiveDaySum