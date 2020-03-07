'''
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))
    
if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Process(target=run_proc,args=('1111',))
    print("Child process will start.")
    p.start()
    #p.join()
    print('Child process end.')


from multiprocessing import Process
import os


def run_proc_1(name):
    print('%s this is process one (%s).'% (name,os.getpid()))

def run_proc_2(name):
    print('%s this is process two (%s).'% (name,os.getpid()))

if __name__=='__main__':
    print('Parent process....%s'% os.getpid())
    p1=Process(target=run_proc_1,args=(1,))
    p2=Process(target=run_proc_2,args=(2,))
    print('Child process will run...')
    p2.start()
    p1.start()
    
    p2.join()
    p1.join()
    print('All is end.')
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.randint(3,8))
    end=time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__=='__main__':
    print('Parent process %s.'% os.getpid())
    p = Pool(4)
    for i in range(9):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')