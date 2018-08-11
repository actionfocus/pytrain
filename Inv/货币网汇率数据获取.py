# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:19:15 2018

@author: actionfocus
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
        count = 0
        for child in soup.tbody.children:
            if count==4:
                #print child
                level = 0
                for item in child.tbody.children:
                    if (level==1 and count==4):
                        print str(item.contents[0].string)
                        print float(item.contents[1].string)
                    level=level+1
            count=count+1
            #print count
            #print child.contents[3].string #美元离岸人民币 最新价
        
def main():
    url = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/html/cn/historyParityCn.html" #离岸汇率
    getContent(url,'OffshoreCNY')
    
if __name__ == '__main__':
    main()

