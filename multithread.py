#!/usr/bin/env python

from Queue import Queue
from threading import Thread

import os
import sys

class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try: func(*args, **kargs)
            except Exception, e: print e
            self.tasks.task_done()

class ThreadPool:
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads): Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()

if __name__ == '__main__':
	
    # 1) Init a Thread pool with the desired number of threads
    pool = ThreadPool(int(THREADS))
    
    data=[]
    chrs = open(CHRO)
    for line in chrs:
        l = line.split()[1:]
        data.append([l[0][3:], l[1][3:]])

    # 2) Add the task to the queue
    for chr in data:
	pool.add_task(call,chr[0], chr[1])
    
    # 3) Wait for completion
    pool.wait_completion()

