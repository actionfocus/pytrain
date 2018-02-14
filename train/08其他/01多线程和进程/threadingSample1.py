# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:57:55 2018

@author: actionfocus
"""
#创建thread的实例，传递给它一个函数
#下面是个例子。实际应用中，多线程更多适用于IO密集型的应用来提高效率

import threading
from time import sleep, ctime
loops = [4,2]
def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    
def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        #将函数名传给target参数，args是target被赋值的函数中需要的惨呼
        t = threading.Thread(target = loop, args = (i, loops[i]))
        threads.append(t)
    
    for i in nloops:
        #调用线程的start()方法让他们开始执行
        threads[i].start()
    
    for i in nloops:
        #为每个线程调用join()方法，等待线程结束，或者在提供了超时间的情况下，达到超时时间。
        #对于 join()方法而言，其另一个重要方面是其实它根本不需要调用。一旦线程启动，
        #它们就会一直执行，直到给定的函数完成后退出。如果主线程还有其他事情要去做，而不是等待
        #这些线程完成（例如其他处理或者等待新的客户端请求），就可以不调用 join()。join()方法只
        #有在你需要等待线程完成的时候才是有用的。
        threads[i].join()
    
    print 'all DONE at:', ctime()
    
if __name__ == '__main__':
    main()
        
