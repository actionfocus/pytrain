# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:34:24 2018

@author: actionfocus
"""

list = ['cat', 'dog', 'elephant', 'tiger']

print list[0], list[1]

#list的下标为负数时，是倒排寻找存在的元素

print list[-1], list[-2]

#list的中切片语法

print list[1:3]

#取得list的长度
print len(list)

#用下表给list中的元素赋值
list[1] = 'newdog'

print list

#通过值来查找元素在列表中的位置
print "newdog is in the position of list as " + str(list.index('newdog'))
print "tiger is in the position of list as " + str(list.index('tiger'))

#list的直接操作
array = [1,2,3]
print list + array

#list中元素重复n
print array * 3
print list * 4

#删除list中的元素
del array[2]
del list[2:4]
print array
print list

#创建循环
for i in range(10):
    print i
    

#确定值是否在list中
if "cat" in list:
    print "True"
if "dog" not in list:
    print "False"
    

#多重赋值
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print size, color, disposition

#append(), insert(), remove()，sort()方法
list.append('last animal')
list.insert(0,'first animal')
print list
list.remove('cat')
print list
list.sort()
print list


#Python传递引用会直接改变list中的值，所以用copy和deepcopy的方法保存一份原list
def egg(para):
    para.append('hello')
spam = [1,2,3]
egg(spam)
print spam #理论上spam只是作为参数传递给egg，不应该更新list，但是实际上在spam上增加了

#copy方法
import copy
newspam = copy.copy(spam) #如果要复制的列表中包含了列表，使用copy.deepcopy()函数
print newspam
