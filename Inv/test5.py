# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:04:06 2018

@author: actionfocus
"""

import tushare as ts

start='2018-05-19'
end='2018-06-15'
code = '159957'

df=ts.get_k_data(code,start=start,end=end)

print df
