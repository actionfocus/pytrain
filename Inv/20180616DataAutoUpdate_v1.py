# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:13:53 2018

@author: ationfocus

v1:依据汇率和十年期国债的数据分析宏观情况

"""


import pymysql
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import tushare as ts
import datetime

PhantomJSPATH = "C:/phantomjs-2.1.1-windows/bin/phantomjs.exe"

def getHTMLText(url):
    driver = webdriver.PhantomJS(executable_path=PhantomJSPATH)
    try:
        driver.get(url)
        time.sleep(1) #必须适当延时，否则无法加载数据到page source的html里面
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        driver.close()
        return soup
    except:
        return "Error Occured in getHTMLText.\n"
    
def getContent(url,record):
    soup = getHTMLText(url)
    if record=='USDCNY':
        count = 0
        for child in soup.tbody.children:
            if count==4:
                #print child
                level = 0
                for item in child.tbody.children:
                    if (level==1 and count==4):
                        t1=( str(item.contents[0].string),float(item.contents[1].string))
                    level=level+1
            count=count+1
        return t1    
    if record=='BondReturn':
#        print soup
        count = 0
        for child in soup.tbody.children:
            if count==0:
                t1=(str(child.contents[0].string), float(child.contents[2].string)) #十年期收益
            count=count+1
        return t1


#抓取最近一个交易日十年国债收益数据
url = "http://www.chinamoney.com.cn/chinese/sddsintigy/" #十年期国债收益率
rs=getContent(url,'BondReturn')
Interest=rs[1]
InterestDate=rs[0]
#抓取最近一个交易日人民币美元汇率数据(来自中国货币网，非离岸数据)
url = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/html/cn/historyParityCn.html" #汇率
rs=getContent(url,'USDCNY')
Exchange=rs[1]
ExchangeDate=rs[0]

#抓取最近一个交易日上证、中证指数
todayDateTime = datetime.datetime.now()

todayDate = todayDateTime.strftime('%Y-%m-%d')

tradeDay = ts.trade_cal()

isTradeDay = tradeDay[(tradeDay['calendarDate']==todayDate)]['isOpen'].values[0]

count = -1 #往回找交易日的日期
while not isTradeDay:
    #print 'find previous trade day...'
    previousDateTime = todayDateTime + datetime.timedelta(days=count)
    previousDate = previousDateTime.strftime('%Y-%m-%d')
    isTradeDay = tradeDay[(tradeDay['calendarDate']==previousDate)]['isOpen'].values[0]
    count = count-1
    
#print previousDate

if count<-1:
    recDate = previousDate
else:
    recDate = todayDate
    
df = ts.get_index()

cnIndex=df[(df['code']=='000905')]['close'].values[0] #使用时，该值必须配合recDate一起返回

shIndex=df[(df['code']=='000001')]['close'].values[0] #使用时，该值必须配合recDate一起返回

#print recDate
#print ExchangeDate
#print InterestDate

if (recDate==ExchangeDate and recDate==InterestDate):

    # Open database connection
    db = pymysql.connect(host='localhost', user='root', password='stockdata', db='stock')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.

    #基础数据表更新

    sql = """INSERT INTO intexchg(recDate,Interest, Exchange, shIndex, cnIndex) 
         VALUES ('%s',%f,%f,%f,%f)"""

    data = (recDate,Interest, Exchange, shIndex, cnIndex)

    try:
        # Execute the SQL command
        cursor.execute(sql % data)
        # Commit your changes in the database
        db.commit()
        print 'recDate=',recDate,'Interest=',Interest,'Exchange=',Exchange,\
                'shIndex=',shIndex,'cnIndex=',cnIndex
        print 'Upload data in success.'
    except:
        # Rollback in case there is any error
        db.rollback()
        print "intexchg update error."

    # disconnect from server
    db.close()

else:
    print 'Interest Data, Exchange Date and Stock Index Date are not synchronzied.'