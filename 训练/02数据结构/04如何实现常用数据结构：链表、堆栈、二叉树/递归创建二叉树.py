# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:57:05 2018

@author: actionfocus
"""
class node():
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class biTree():
    
    rootnode = None
    
    def InsertNode(self, root, x):
        if root == None:
            pnode = node()
            pnode.val = x
            pnode.left = None
            pnode.right = None
            root = pnode
        elif (x < root.val):
            root.left = self.InsertNode(root.left, x)
        else:
            root.right = self.InsertNode(root.right, x)
        return root
    
    def SetupBiTree(self):
        
        list = [15,5,3,12,16,20,23,13,18,10,6,7]
        for item in list:
            self.rootnode = self.InsertNode(self.rootnode, item)
            
    def display(self):
        print self.rootnode.val
        print self.rootnode.left.left.val
        print self.rootnode.right.right.val
    
if __name__ == '__main__':
    bt = biTree()
    bt.SetupBiTree()
    bt.display()
        