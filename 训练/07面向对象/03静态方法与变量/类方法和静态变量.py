# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:06:51 2018

@author: actionfocus
"""
#类方法是将类本身作为对象进行操作的方法。使用@classmethod装饰器定义。

class Times(object):
    factor = 1
    @classmethod
    def mul(cls, x):    #类是作为第一个参数(cls)传递的
        return cls.factor*x
    
class TwoTimes(Times):
    factor = 2
    

x=TwoTimes.mul(4)
print x

'''目前了解Python中没有类似于Java中的静态变量'''
