# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 20:45:13 2018

@author: 
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
        time.sleep(2) #必须适当延时，否则无法加载数据到page source的html里面
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        driver.close()
        return soup
    except:
        return "Error Occured in getHTMLText.\n"
    
#url = "http://quote.eastmoney.com/centerv2/whsc/rmbpz/rmbhlzjj" #人民币汇率
#url = "http://quote.eastmoney.com/centerv2/qqzs/mzgs" #美洲股市
#url = "http://quote.eastmoney.com/centerv2/hjsc/gjgjsxh" #贵金属
#url = "http://quote.eastmoney.com/centerv2/qhsc/gjqh/UF_NYMEX_CL" #原油期货
#url = "http://data.eastmoney.com/cjsj/hyzs.html" #行业指数
url = "http://data.eastmoney.com/cjsj/globalRate.html" #利率        
soup = getHTMLText(url)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#for child in soup.tbody.children:
#    print type(child)
#    print type(child.contents)
#    print dir(child.contents)
#    print type(child.contents[0])
#    print child.contents
#汇率
#    print child.contents[1].string, "\t", child.contents[2].string 
#股票市场    
#    print child.contents[0].a.string, "\t", child.contents[1].string, "\t", child.contents[9].string
#贵金属
#    print child.contents[1].string, "\t", child.contents[2].string, "\t", child.contents[3].string, "\t", float(child.contents[3].string)/28.35, "\t", child.contents[10].string
#原油期货
#    print child.contents[1].string, "\t", child.contents[2].string, "\t", child.contents[3].string
#行业指数
#    print child.contents[1].a.string, "\t", child.contents[2].string, "\t", child.contents[3].string, "\t", child.contents[4].string, "\t", child.contents[6].string


#处理利率页面的代码
result = soup.find_all('tbody')
#print result[1]
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