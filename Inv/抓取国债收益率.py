# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 23:41:16 2018

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
    if record=='BondReturn':
#        print soup
        for child in soup.tbody.children:
            print child.contents[0].string #日期
            print child.contents[1].string #一年期收益
            print child.contents[2].string #十年期收益
#            print child.contents[1].a.string, "\t", child.contents[2].string, "\t", child.contents[3].string, "\t", child.contents[4].string, "\t", child.contents[6].string
            
        
def main():
    url = "http://www.chinamoney.com.cn/chinese/sddsintigy/" #行业指数
    getContent(url,'BondReturn')
    
if __name__ == '__main__':
    main()
