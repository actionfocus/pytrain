# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:23:51 2018

@author: actionfocus
"""


import time
#import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
#import pandas as pd

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
    extractTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if record=='exchangeRate':
        for child in soup.tbody.children:
            print child.contents[1].string, "\t", child.contents[2].string,"\t", extractTime
    if record=='Stock':
        for child in soup.tbody.children:
            print child.contents[0].a.string, "\t", child.contents[1].string, "\t", child.contents[9].string
    if record=='preciousMetal':
        for child in soup.tbody.children:
            print child.contents[1].string, "\t", child.contents[2].string, "\t", child.contents[3].string, "\t", float(child.contents[3].string)/28.35, "\t", child.contents[10].string
    if record=='futureOil':
        for child in soup.tbody.children:
            print child.contents[1].string, "\t", child.contents[2].string, "\t", child.contents[3].string
    if record=='interest':
        result = soup.find_all('tbody')
        count = 2
        for child in result[0].children:
            if count%2 == 1:
                print child.contents[1].string,"\t",child.contents[3].string,"\t",child.contents[5].string,"\t",child.contents[11].string
            count = count + 1
    
        count = 2    
        for child in result[1].children:
            if count%2 == 1:
                print child.contents[1].string,"\t",child.contents[3].string,"\t",child.contents[5].string,"\t",child.contents[11].string
            count = count + 1
            
        
def main():
    url = "http://quote.eastmoney.com/centerv2/whsc/rmbpz/rmbhlzjj" #人民币汇率
    getContent(url,'exchangeRate')
    url = "http://quote.eastmoney.com/centerv2/qqzs/mzgs" #美洲股市
    getContent(url,'Stock')
    url = "http://quote.eastmoney.com/centerv2/qqzs/yzgs" #亚洲股市
    getContent(url,'Stock')
    url = "http://quote.eastmoney.com/centerv2/qqzs/ozgs" #欧洲股市
    getContent(url,'Stock')
    url = "http://quote.eastmoney.com/centerv2/qqzs/azgs" #澳洲股市
    getContent(url,'Stock')
    url = "http://quote.eastmoney.com/centerv2/hjsc/gjgjsxh" #贵金属
    getContent(url,'preciousMetal')
    url = "http://quote.eastmoney.com/centerv2/qhsc/gjqh/UF_NYMEX_CL" #原油期货
    getContent(url,'futureOil')
    url = "http://data.eastmoney.com/cjsj/globalRate.html" #利率
    getContent(url,'interest')
    
if __name__ == '__main__':
    main()
        


