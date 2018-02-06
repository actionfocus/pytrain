# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 11:40:13 2018

@author: actionfocus
"""

import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")
print soup.title
tag = soup.a
print tag
print tag.name
print tag.parent.name
print tag.attrs #attrs是一个字典对象
print tag.attrs['href'] #通过访问字典的关键字，获取对应内容
print soup.p.string #返回标签间的非HTML属性字符信息

print soup.head
print soup.head.contents
print soup.body.contents
print "----------------------"

#遍历儿子节点
for child in soup.body.children:
    print child

print "---------------------"    
#遍历子孙节点
for child in soup.body.children:
    print child

print "---------------------"        
#标签树的上行遍历
for parent in soup.a.parents:
    if parent is None:
        print parent
    else:
        print parent.name
print "---------------------"           
#平行遍历发生在同一个父节点的各节点之间
print soup.a.next_sibling
print soup.a.next_sibling.next_sibling
print "---------------------"   
print soup.a.previous_sibling
print soup.a.previous_sibling.previous_sibling
print "---------------------"
#平行遍历后续节点
for sibling in soup.a.next_siblings:
    print sibling
print "---------------------"
#平行遍历前序节点
for sibling in soup.a.previous_siblings:
    print sibling
print "---------------------"

#查找demo页面中所有的链接
#<>.find_all(name, attrs, recursive, string, **kwargs)
for link in soup.find_all('a'):
    print link.get('href')

print "---------------------"    
