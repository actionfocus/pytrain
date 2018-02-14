# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 22:57:15 2018

@author: actionfocus
"""

import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

PhantomJSPATH = "C:/phantomjs-2.1.1-windows/bin/phantomjs.exe"

def getHTMLText(url):
    driver = webdriver.PhantomJS(executable_path=PhantomJSPATH)
    try:
        driver.get(url)
        time.sleep(3) #必须适当延时，否则无法加载数据到page source的html里面
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        driver.close()
        return soup
    except:
        return "Error Occured in getHTMLText.\n"
    
    
def getPEratio():
    url = "http://www.sse.com.cn/market/stockdata/overview/day/"
    soup = getHTMLText(url)
    
    dateList=[]
    drqkList=[] #单日情况
    astockList=[] #A股情况
    
    items = soup.find_all('div', class_="sse_table_title2") #注意class后面有个_符号
    result = items[0].string[-10:]
    date = datetime.datetime.strptime(result,"%Y-%m-%d")
    
    count = 1
    for child in soup.tbody.children:
        if (count == 1): #跳出原页面中的第一个空行
            print "skip.\n"
        else:
            dateList.append(date)
            drqkList.append(child.contents[0].string)
            peValue=child.contents[2].string
            if peValue <> '-':
                astockList.append(float(child.contents[2].string))
            else:
                peValue=0
                astockList.append(peValue)
        count = count + 1

    record = {'date':dateList,'drqk':drqkList,'astock':astockList}
    df = pd.DataFrame(record)
    print df
    print df.iloc[0:1,0:1]
    print df.loc[0:0]
    
def main():
    getPEratio()
    
if __name__ == '__main__':
    main()
        