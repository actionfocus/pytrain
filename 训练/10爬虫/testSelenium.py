# -*- coding: utf-8 -*-
"""
Created on Sat Feb 03 14:18:05 2018

@author: actionfocus
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.PhantomJS(executable_path="C:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
#driver = webdriver.Chrome()
driver.get("http://www.sseinfo.com/services/other/peratio/")
#elem = driver.find_element_by_name("wd")
#elem.clear()
#elem.send_keys(u'地图')
#elem.send_keys(Keys.RETURN)
#driver.close()
time.sleep(3) #必须适当延时，否则无法加载数据到page source的html里面
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#print soup.prettify()
driver.close()

dateList=[]
industryList=[]
peList=[]

items = soup.find_all('div', class_="system_date") #注意class后面有个_符号
result = items[0].string[-10:]
date = datetime.datetime.strptime(result,"%Y-%m-%d")

count = 1
for child in soup.tbody.children:
    #print type(child)
    #print count
    if (count == 1): #跳出原页面中的第一个空行
        print "skip\n"
    else:
        dateList.append(date)
        industryList.append(child.contents[0].string)
        peList.append(child.contents[2].string)
    count = count + 1
    print "-----\n"

record = {'date':dateList,'industry':industryList,'PEstatic':peList}
df = pd.DataFrame(record)
print df