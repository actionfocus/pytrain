# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import re

#一次用多个股票代码请求腾讯接口数据
result = requests.get('http://qt.gtimg.cn/q=sh601919,hk01919,sz002400,sh601818')

#将多行数据进行拆分
m = re.split('\n',result.text.rstrip('\n'))
print len(m)
for item in m:
    print item
    print "----"

#取其中一个股票代码返回的数据进行下一步的拆分    
line = m[1]

#根据字符串结构，用“=”进行拆分成两部分
parts = re.split('=',line)
print parts[0], '\n', parts[1]

#根据返回值特点，用"~"进行分割拆分
quotes = re.split('~',parts[1])

#其中[1]为股票名称，[2]为股票代码，[3]为股票当前价格，具体参考
#http://blog.csdn.net/robertsong2004/article/details/46340621对接口API数据的说明
print quotes[1],quotes[2],quotes[3]