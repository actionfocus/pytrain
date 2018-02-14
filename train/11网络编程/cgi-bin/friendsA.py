# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:33:03 2018

@author: actionfocus
"""

import cgi

reshtml = '''Content-Type: text/html\n
    <HTML>
        <HEAD><TITLE>
        Friends CGI demo
        </TITLE></HEAD>
        <body>
            <h3>Friends list for:<i>%s</i></h3>
            your name is: <b>%s</b><p>
            you have <b>%s</b> friends.
        </body>
    </HTML>'''
    
form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who, who, howmany)