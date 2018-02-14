# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:49:24 2018

@author: actionfocus
"""

#静态方法是一种普通函数，只不过他们正好位于类定义的命名空间中，不会对任何实例类型
#   进行操作。
#如果在编写类时需要采用很多不同的方式来创建新实例，则常常使用静态方法，因为类中只有
#一个__init__()函数。

import time

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod #静态方法标记
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

print time.localtime() 
a = Date(1992, 2, 3)
b = Date.now()
c = Date.tomorrow()
print str(a.year)+"/"+str(a.month)+"/"+str(a.day)
print str(b.year)+"/"+str(b.month)+"/"+str(b.day)
print str(c.year)+"/"+str(c.month)+"/"+str(c.day)