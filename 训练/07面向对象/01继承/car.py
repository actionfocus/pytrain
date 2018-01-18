# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:50:07 2018

@author: actionfocus
"""

#驼峰命名法：类名中的每个单词的首字母大写，不使用下划线。实例名和模块名都采用小写格式，
#           并在单词之间加上下划线

class Car(object):
    #python 3语法下，父类class()里面不需要写object，在python 2.7里是为了与子类进行
    #   关联，子类的super()需要两个实参，子类名和对象self
    """try on car class"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class Battery():
    """把电瓶属性单独抽取出来做一个类"""
    
    def __init__(self, battery_size=70):
        "初始化电瓶的属性"
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print "This car has a " + str(self.battery_size) + "-kWh battery."
    
    def get_range(self):
        """打印一条描述电瓶续航里程的信息"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print message
        
class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        #python 3的语法下，下面这句话直接用super().__init__(make, model, year)
        super(ElectricCar,self).__init__(make, model, year)
        self.battery = Battery()
        