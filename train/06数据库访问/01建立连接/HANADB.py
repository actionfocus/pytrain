# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:20:36 2018

@author: actionfocus
"""
import pyhdb

def get_connection():
    conn_obj = pyhdb.connect(
        host="192.168.1.13",
        port=30415,	#port的编号是3+instance number+15
        user="SYSTEM",
        password="Txelservre1"
    )

    return conn_obj
def get_items(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM DATA_TYPES')
    items = cursor.fetchall()

    return items

conn = get_connection()
items = get_items(conn)
for item in items:
    print item