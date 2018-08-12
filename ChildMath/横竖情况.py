# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 14:57:28 2018

@author: actionfocus

#解决的问题：
火柴棒有n根，每根有横、竖两种摆法，n根火柴棒可以组成多少组图形

"""
list = ['——','|']

#list = ['——','|','/'] #可以拓展为火柴棒三种摆法的情形

#方法一：循环算法，需要手工修改变量和循环层次
#count=1
#for stick1 in list:
#    for stick2 in list:
#        for stick3 in list:
#            for stick4 in list:
#                print count, stick1, stick2, stick3, stick4, '\n'
#                count = count+1


#方法二：递归算法，不需要手工增加变量和修改程序结构

def disp(n):
#    count=1
    res1=[]
    res2=[]
    if n==1:
        for stick in list:
            res1.append(stick)
        return res1
    else:
        for stick in list:
            for each in disp(n-1):
                item = each+' '+stick
                res2.append(item)
        return res2

#disp(n)中n为火柴棒的个数    
res3 = disp(4)

count=1
for each in res3:
    print count, ' ', each
    count=count+1
