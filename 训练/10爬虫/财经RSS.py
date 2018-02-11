# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:17:55 2018

@author: actionfocus
"""

import feedparser as fd

def setupFeed(url):
    feed = fd.parse(url)
    return feed

def getTitle(feed):
    for entry in feed.entries:  
        print entry.title
#        print entry.keys()
#        print entry.links
#        print entry.link
        url = entry.link
        print url
        
def main():
    url = "http://rssft.com/emoney/cjdd.xml"
    feed = setupFeed(url)
    getTitle(feed)
    url = "http://rssft.com/emoney/ssgs.xml"
    feed = setupFeed(url)
    getTitle(feed)
    url = "http://rssft.com/emoney/zsdc.xml"
    feed = setupFeed(url)
    getTitle(feed)
    url = "http://rssft.com/emoney/bkjj.xml"
    feed = setupFeed(url)
    getTitle(feed)    
    url = "http://rssft.com/emoney/qsyw.xml"
    feed = setupFeed(url)
    getTitle(feed)  
    url = "http://rssft.com/emoney/syzx.xml"
    feed = setupFeed(url)
    getTitle(feed) 
    url = "http://www.people.com.cn/rss/finance.xml"
    feed = setupFeed(url)
    getTitle(feed) 

    
if __name__ == '__main__':
    main()
