# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:24:45 2018

@author: I311936
"""

import tushare as ts
import pandas as pd
import requests

df1=ts.get_realtime_quotes('601919')
print df1

stockcode = 'hk01919'
url1 = 'http://qt.gtimg.cn/q='+stockcode
result = requests.get(url1)
print result.text

