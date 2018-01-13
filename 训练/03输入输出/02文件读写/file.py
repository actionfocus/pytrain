
# coding: utf-8

# In[5]:

import os

# open(filepath)以读方式打开文件，open(filepath,'w')以写方式打开，open(filepath,'r+')以读写方式打开
# open(filepath, 'rb')以二进制读模式打开

fp = open('C:/laptop/00Python/testdata/file.txt', 'r+')
for line in fp.readlines():
    print line.strip()
fp.close()

filename = raw_input('Enter file path and name: ')
f = open(filename, 'r')
allLines = f.readlines()
print allLines
f.close()


#导入了os模块后，变量linesep表示“用于在文件中分隔行的字符串”；变量sep表示“用来分隔文件路径名的字符串”；变量pathsep表示“用于分隔文件路径的字符串”
#变量curdir表示“当前工作目录的字符串名称”；变量pardir表示“（当前工作目录的）父目录字符串名称”
filename = raw_input('Enter file name: ')
fobj = open(filename, 'w')
while True:
    aLine = raw_input("Enter a line ('.' to quit): ")
    if aLine != ".":
        fobj.write('%s%s' % (aLine, os.linesep))
    else:
        break
fobj.close()
print fobj.mode
print fobj.name
print fobj.closed
print fobj.encoding
print fobj.newlines

