# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:24:09 2018

@author: I311936
"""

str = "  Sdsf sdsf  "
#print dir(str)

#下面列出字符串的部分方法
#'capitalize', 'center', 'count', 'decode', 'encode', 
#'endswith', 'expandtabs', 'find', 'format', 'index', 
#'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 
#'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
#'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
#'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
#'swapcase', 'title', 'translate', 'upper', 'zfill'

print str.capitalize()
print str.count('ds',1,7)
print str.find('s',1,7)
print str.isalnum()
print str.isalpha()
print str.isdigit()
print str.islower()
print str.split('ds') #结果为['s', 'fs', 'f']
print str.swapcase()
print str.strip(), len(str.strip())
print str.lstrip(), len(str.lstrip())
print str.rstrip(), len(str.rstrip())
print str.upper()
print str.lower()

data = "2018/01/23"
list = data.split('/')
for item in list:
    print item