# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 09:18:31 2018

@author: actionfocus

离岸美元/人民币汇报获取

数据来源：东方财富网
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver

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
#    extractTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if record=='OffshoreCNY':
#        print soup
        for child in soup.tbody.children:
            print child.contents[3].string #美元离岸人民币 最新价
        
def main():
    url = "http://quote.eastmoney.com/center/gridlist.html#forex_cnh" #离岸汇率
    getContent(url,'OffshoreCNY')
    
if __name__ == '__main__':
    main()



