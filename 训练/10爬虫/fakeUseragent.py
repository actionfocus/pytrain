# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:59:07 2018

@author: actionfocus
"""

import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.text
except:
    print "failed."