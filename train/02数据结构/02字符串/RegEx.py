# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:36:08 2018

@author: actionfocus
"""
import re
DATA = (
        'Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA',
        'Bostong 23231 HZ'
        )
for datum in DATA:
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum)