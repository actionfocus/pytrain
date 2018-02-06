# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:53:04 2018

@author: actionfocus
"""

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    kv = {'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url,headers=kv, allow_redirects=True)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error Occured in getHTMLText.\n"

html = getHTMLText("http://www.sseinfo.com/services/other/peratio/")

print html

#infoDict = {}
#soup = BeautifulSoup(html, 'html.parser')
#print soup.prettify()