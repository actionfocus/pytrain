# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:21:41 2018

@author: actionfocus
"""
class AnonymousSurvey():
    
    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_questions(self):
        print question
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print "Survey result:"
        for response in responses:
            print '- '+response
