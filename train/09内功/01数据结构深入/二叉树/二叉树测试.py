# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:24:45 2018

@author: actionfocus
"""

from linkedbst import LinkedBST

tree = LinkedBST()
print "Adding D B A C F E G"
List = ['D','B','A','C','F','E','G']
for item in List:
    tree.add(item)

print '\nTree Structure:\n'
print tree