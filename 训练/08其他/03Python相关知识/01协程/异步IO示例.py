# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:43:51 2018

@author: actionfocus
"""
import select
import types
import collections

class Task(object):
    def __init__(self, target):
        self.target = target #一个协程
        self.sendval = None  #恢复时要发送的值
        self.stack = []    #调用栈
        
    def run(self):
        try:
            result = self.target.send(self.sendval)
            if isinstance (result, SystemCall):
                return result
            if isinstance (result, types.GeneratorType):
                self.stack.append(self.target)
                self.sendval = None
                self.target = result
            else:
                if not self.stack: return
                self.sendval = result
                self.target = self.stack.pop()
        except StopIteration:
            if not self.stack: raise
            self.sendval = None
            self.target = self.stack.pop()

#表示“系统调用”的对象
class SystemCall(object):
    def handle(self, sched, task):
        pass

#调用程序对象
class Scheduler(object):
    def __init__(self):
        self.task_queue = collections.deque()
        self.read_waiting = {}
        self.write_waiting = {}
        self.numtasks = 0
    
    #通过协程新建任务    
    def new(self, target):
        newtask = Task(target)
        self.schedule(newtask)
        self.numtasks += 1
    
    #将任务放入队列
    def schedule(self, task):
        self.task_queue.append(task)
    
    #让任务等待文件描述符上的数据    
    def readwait(self, task, fd):
        self.read_waiting[fd] = task
    
    #让任务等待写入文件描述符
    def writewait(self, task, fd):
        self.write_waiting[fd] = task
    
    #调度程序主循环
    def mainloop(self, count = -1, timeout = None):
        while self.numtasks:
            #检查要处理的I/O事件
            if self.read_waiting or self.write_waiting:
                wait = 0 if self.task_queue else timeout
                r,w,e = select.select(self.read_waiting, self.write_waiting, [], wait)
                for fileno in r:
                    self.schedule(self.read_waiting.pop(fileno))
                for fileno in w:
                    self.schedule(self.write_waiting.pop(fileno))
            
            #运行队列上准备运行的所有任务
            while self.task_queue:
                task = self.task_queue.popleft()
                try:
                    result = task.run()
                    if isinstance(result, SystemCall):
                        result.handle(self, task)
                    else:
                        self.schedule(task)
                except StopIteration:
                    self.numtasks -= 1
            
            #如果没有任务可以运行，是等待还是返回
            else:
                if count > 0 : count -= 1
                if count ==0:
                    return
#实现不同系统的调用                
class ReadWait(SystemCall):
    def __init__(self, f):
        self.f = f
    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.readwait(task, fileno)
        
class WriteWait(SystemCall):
    def __init__(self, f):
        self.f = f
    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.writewait(task, fileno)

class NewTask(SystemCall):
    def __init__(self, target):
        self.target = target
    def handle(self, sched, task):
        sched.new(self.target)
        sched.schedule(task)
        
from socket import socket, AF_INET, SOCK_STREAM

def time_server(address):
    import time
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        yield ReadWait(s)
        conn, addr = s.accept()
        print("Connection from %s" % str(addr))
        yield WriteWait(conn)
        resp = time.ctime() + "\r\n"
        conn.send(resp.encode('latin-1'))
        conn.close()
        
sched = Scheduler()
sched.new(time_server(('', 10000)))
sched.new(time_server(('', 11000)))
sched.run()
            
