# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:34:02 2018

@author: actionfocus
"""

#如果两个线程运行的顺序发生变化，就有可能造成代码的执行轨迹或行为不相同，或者产生
#不一致的数据。这时候需要使用同步。当任意数量的线程可以访问临界区的代码，但在给定
#的时刻只有一个线程可以通过时，就是使用同步的时候。Python支持多种同步类型，可以给
#足够的选择，以便完成合适的任务类型。

#锁，是最简单、最低级的机制。
#信号量用于多线程竞争有限资源的情况。

#下面是锁例子

#python 2.5以后可以不用再调用锁的acquire()和release()方法，使用with语句

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)
    
loops = (randrange(2,5) for x in xrange(randrange(3,7)))
    
remaining = CleanOutputSet()
lock = Lock()
    
def loop(nsec):
   myname = currentThread().name
   lock.acquire()
   remaining.add(myname)
   print '[%s] Started %s' % (ctime(), myname)
   lock.release()
   sleep(nsec)
   lock.acquire()
   remaining.remove(myname)
   print '[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)
   print ' (remaining:%s)' % (remaining or 'NONE')
   lock.release()

#with语句示例
#from __future__ import with_statement
#def loop(nsec):
#    myname = currentThread().name
#    with lock:
#        remaining.add(myname)
#        print '[%s] Started %s' % (ctime(), myname)
#    sleep(nsec)
#    with lock:
#        remaining.remove(myname)
#        print '[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)
#        print ' (remaining: %s)' % (remaining or 'NONE',)
        
def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()
    
@register
def _atexit():
   print 'all DONE at:', ctime()
   
if __name__=='__main__':
    _main()