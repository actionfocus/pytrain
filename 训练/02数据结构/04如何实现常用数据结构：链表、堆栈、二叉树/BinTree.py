# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:07:46 2018

@author: Actionfocus
"""

class Node():
    def __init__(self, data=None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree():
    def InitBiTree(self):
        #参数：&T
        #操作结果：构造空二叉树T
        self.root = Node()
        self.myQueue = []
        
#    def DestoryBiTree():
#        #参数：&T
#        #初始条件：二叉树存在
#        #操作结果：销毁二叉树T
#        
    def CreateBiTree(self, datasource):
        #参数：&T, definition
        #初始条件：参数definition给出二叉树的定义
        #操作结果：按definition构造二叉树
        for item in datasource:
            node = Node(item)
            if self.root.data == None:
                self.root = node
                self.myQueue.append(self.root)
            else:
                treeNode = self.myQueue[0]
                if treeNode.left == None:
                    treeNode.left = node
                    self.myQueue.append(treeNode.left)
                else:
                    treeNode.right = node
                    self.myQueue.append(treeNode.right)
                    self.myQueue.pop(0)

            
#    
#    def ClearBiTree():
#        #参数：&T
#        #初始条件：二叉树存在
#        #操作结果：将二叉树T清为空树
#    
#    def BiTreeEmpty():
#        #参数：T
#        #初始条件：二叉树T存在
#        #操作结果：若T为空二叉树，则返回True，否则返回FALSE
#    
#    def BiTreeDepth():
#        #参数：T
#        #初始条件：二叉树T存在
#        #操作结果：返回T的深度
#        
#    def Root():
#        #参数：T
#        #初始条件：二叉树存在
#        #操作结果：返回T的根
#    
#    def Value():
#        #参数：T，e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：返回e的值
#    
#    def Assign():
#        #参数:T, &e, value
#        #初始条件：二叉树T存在，e是T中的某个结点
#        #操作结果：结点e赋值为value
#    
#    def Parent():
#        #参数：T，e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：若e是T的非根结点，则返回它的双亲，否则返回"空“
#    
#    def LeftChild():
#        #参数：T, e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：返回e的左孩子。若e无左孩子，则返回"空“
#        
#    def RightChild():
#        #参数：T,e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：返回e的右孩子。若e无右孩子，则返回"空“
#        
#    def LeftSibling():
#        #参数：T,e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：返回e的左兄弟结点。若e是T的左孩子或无左兄弟，则返回空
#    
#    def RightSibling():
#        #参数：T,e
#        #初始条件：二叉树T存在，e是T中某个结点
#        #操作结果：返回e的右兄弟结点。若e是T的右孩子或无右兄弟，则返回空
#    
#    def InsertChild():
#        #参数：T, p, LR, c
#        #初始条件：二叉树T存在，p指向T中某个结点，LR为0或者1，
#        #         非空二叉树c与T不相交且右子树为空
#        #操作结果：根据LR为0或者1，插入c为T中p所指结点的左或右子树。p所指结点的
#        #         原有左或右子树则成为c的右子树。
#    
#    def DeleteChild():
#        #参数： T, p, LR
#        #初始条件：二叉树T存在，p指向T中某个结点，LR为0或1.
#        #操作结果：根据LR为0或1，删除T中p所指结点的左或右子树。
#    
#    def PreOrderTraverse():
#        #参数：T, visit()
#        #初始条件：二叉树T存在，Visit是对结点操作的应用函数。
#        #操作结果：先序遍历T，对每个结点调用函数Visit一次且仅一次。
#        #       一旦visit()失败，则操作失败。
#    
#    def InOrderTraverse():
#        #参数：T, Visit()
#        #初始条件：二叉树T存在，Visit是对结点操作的应用函数。
#        #操作结果：中序遍历T，对每个结点调用函数Visit一次且仅一次。
#        #       一旦visit()失败，则操作失败。
#        
#    def PostOrderTraverse():
#        #参数：T, Visit()
#        #初始条件：二叉树T存在，Visit是对结点操作的应用函数。
#        #操作结果：后序遍历T，对每个结点调用函数Visit一次且仅一次。
#        #       一旦visit()失败，则操作失败。
#        
#    def LevelOrderTraverse():
#        #参数：T, Visit()
#        #初始条件：二叉树T存在，Visit是对结点操作的应用函数。
#        #操作结果：层序遍历T，对每个结点调用函数Visit一次且仅一次。
#        #       一旦visit()失败，则操作失败。
        
if __name__ == '__main__':
    BiTree = BinaryTree()
    BiTree.InitBiTree()
#    print BiTree.root.data
    list = [1,2,3,4,5,6]
    BiTree.CreateBiTree(list)
    print BiTree.root.data
    print BiTree.root.left.data
    print BiTree.root.right.data
    print BiTree.myQueue[0].data
    print BiTree.myQueue[0].left.data
    print BiTree.myQueue[0].right
    del BiTree
    