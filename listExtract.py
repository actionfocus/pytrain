# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:51:47 2017

@author: I311936
"""

#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import tushare as ts
df=ts.get_hist_data('60016')
print df