# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:28:06 2018

@author: actionfocus
"""

#对类进行测试的例子

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    #先做setUp进行对象实例化，下面例子是先建立my_survey对象
    #然后，再运行test开头的方法，这样在每个测试方法中都可以使用setUp()中创建的对象
    
    def setUp(self): #注意Up的"U"要大写
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses= [ 'English','Spanish','Mandarin' ]
        
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
unittest.main()
        
