#coding=utf-8
import time
from threading import Thread
'''两上不同的thread方法同时启动'''
def get_list():  #曲线菜单列表
    dict={"历史曲线":"功率曲线展示,历史曲线"}
    return dict
def find_list(menu):  #查找某一菜单
    get_list()
    for key, value in get_list().items():
        if menu == key:
            # print((get_list()[key]).split(','))
            return (get_list()[key]).split(',')
class MyThread(Thread): #多线程方法重写
    def __init__(self, menu):
        Thread.__init__(self)
        self.menu = menu
    def run(self):
        self.result = find_list(self.menu)
    def get_result(self):
        return self.result,time.time()
class MyThreadt(Thread):
    def __init__(self, menu):
        Thread.__init__(self)
        self.menu = menu
    def run(self):
        self.result = find_list(self.menu)
    def get_result(self):
        return self.result,time.time()

if __name__ == '__main__':
    thd1 = MyThread('历史曲线')
    thd2 = MyThreadt('历史曲线')
    thd1.start()
    thd2.start()
    thd1.join()
    thd2.join()
    print (thd1.get_result())
    print (thd2.get_result())

