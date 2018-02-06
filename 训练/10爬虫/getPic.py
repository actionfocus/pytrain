# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:35:49 2018

@author: actionfocus
"""

import requests
import os
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1517423279737&di=f5c995d6da4d421e7594882a590823c6&imgtype=0&src=http%3A%2F%2Fimg01.taopic.com%2F160621%2F318762-1606211009258.jpg"
root = "c:/Temp/"
path = root + url.split('-')[-1]
try:
    kv = {'user-agent':'Mozilla/5.0'}
    
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,headers=kv)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print "File Saved."
    else:
        print "File Exists."
except:
    print "Failed."

