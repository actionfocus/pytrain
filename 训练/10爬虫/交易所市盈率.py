# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 12:10:34 2018

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
    url = "http://www.sseinfo.com/services/other/peratio/"
    soup = getHTMLText(url)
    
    dateList=[]
    industryList=[]
    peList=[]
    
    items = soup.find_all('div', class_="system_date") #注意class后面有个_符号
    result = items[0].string[-10:]
    date = datetime.datetime.strptime(result,"%Y-%m-%d")
    
    count = 1
    for child in soup.tbody.children:
        if (count == 1): #跳出原页面中的第一个空行
            print "skip.\n"
        else:
            dateList.append(date)
            industryList.append(child.contents[0].string)
            peValue=child.contents[2].string
            if peValue <> '-':
                peList.append(float(child.contents[2].string))
            else:
                peValue=0
                peList.append(peValue)
        count = count + 1

    record = {'date':dateList,'industry':industryList,'PEstatic':peList}
    df = pd.DataFrame(record)
    print df.sort_values(by='PEstatic')
    
def main():
    getPEratio()
    
if __name__ == '__main__':
    main()
        


