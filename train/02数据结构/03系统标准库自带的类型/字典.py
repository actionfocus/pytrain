# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:17:08 2018

@author: actionfocus
"""

#字典使用大括号来安排键-值对
mycat = {'size':'fat','color':'gray','disposition':'loud'}
print mycat['size']

#两个列表之间的元素顺序都一致时才时相等的，而两个字段只要键值对一致，就是相同的
newcat = {'color':'gray','disposition':'loud','size':'fat'}
print mycat == newcat

list1 = [1,2,3]
list2 = [1,3,2]
print list1 == list2

#用in, not in检查字符串是否在字典中
str = 'size'
if str in mycat.keys():
    print "True"
    print str+" value is "+mycat[str]

if str in mycat.values():
    print "impossible"
else:
    print str+" is not in dictionary values."
    
#字典中keys(), values()和items()方法
for k in mycat.keys():
    print k

for v in mycat.values():
    print v

for k, v in mycat.items():
    newstr = "Key: "+k+" value is: "+v
    print newstr

#字典中的get(), setdefault()方法
print mycat.get('color','no value') #'no value'是get()方法中如果字典没有'color'
                                    #这样的key，默认返回后面该值
print mycat.get('si','no this key value')

mycat.setdefault('location', 'Shanghai')

print mycat #'location'这个key之前没有，默认值设置为‘Shanghai'.

mycat.setdefault('location','Beijing')

print mycat #因为location这个key中已经有值，所有不会再用新值进行覆盖
