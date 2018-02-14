# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:55:11 2018

@author: actionfocus
"""
#对函数进行测试的例子

#正常项目中下面这个被测试函数，是单独在另外一个py文件中，用from xxx import get_formatted_name来导入

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

import unittest

class NameTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
