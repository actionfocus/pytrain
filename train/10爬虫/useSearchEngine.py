# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:25:55 2018

@author: actionfocus
"""

import requests
keyword = '中信证券'
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    
    #360的搜索代码
    #kv = {'q': keyword}
    #r = requests.get("http://www.so.com/s", params=kv)
    
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print "failed."