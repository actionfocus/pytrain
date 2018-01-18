# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:08:18 2018

@author: actionfocus
"""
from car import ElectricCar

my_tesla = ElectricCar('tesla','model s','2016')

print my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
