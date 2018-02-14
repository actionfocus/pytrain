# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:44:51 2018

@author: actionfoucus
"""

from abc import abstractmethod,ABCMeta,abstractproperty

class All_file:
    __metaclass = ABCMeta
    all_type='file'
    @abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

txt_file=Txt()

sata_file=Sata()

process_file=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
txt_file.read()
sata_file.write()
process_file.read()

print(txt_file.all_type)
print(sata_file.all_type)
print(process_file.all_type)