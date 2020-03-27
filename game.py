from multiprocessing import Pool,pool

import random,os,time

def ant_run():
    class Ant(object):
        @property
        def run(self):
            num=random.random()*3
            time.sleep(num)
            print('子线程 %s ,运行了 %2f 秒.'%(os.getpid(),num))
            return num
    a=Ant()
    num=a.run
    return num
list_name=['name_%s'%i for i in range(15)]

if __name__=='__main__':
    p=Pool()
    for i in range(15):
        list_name[i]=p.apply_async(ant_run)
    print('准备！')
    p.close()
    p.join()
    list_out=[list_name[i].get() for i in range(15)]
    print(list_out)


    
