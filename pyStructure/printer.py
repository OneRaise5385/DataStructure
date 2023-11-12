from structures import Queue
import random

class Printer():
    '''打印机类'''
    def __init__(self,ppm):
        '''初始化打印速度，打印机状态，打印持续时间'''
        self.pagerate = ppm     # 打印速度
        self.currentTask = None
        self.timeRaimaining = 0

    def tick(self):
        '''打印一秒'''
        if self.currentTask != None:
            self.timeRaimaining -= 1
            if self.timeRaimaining <= 0:
                self.currentTask = None

    def busy(self):
        '''判断打印机是否忙'''
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self,newtask):
        '''打印新作业'''
        self.currentTask = newtask
        self.timeRaimaining = newtask.pages * 60 / self.pagerate

class Task():
    '''打印任务类'''
    def __init__(self,time):
        '''初始化：时间戳，生成随机的每次打印的次数'''
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        '''获取时间戳'''
        return self.timestamp
    
    def getPages(self):
        '''获取每次打印的页数'''
        return self.pages
    
    def waitTime(self,currenttime):
        '''等待的时间'''
        return currenttime - self.timestamp
    
# 模拟打印任务
def newPrintTask():
    '''随机生成打印任务'''
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False
    
def simulation(numSeconds,pagesPerMinute):
    '''模拟打印任务'''
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        # 如果随机生成了打印任务，则创建任务并且加入打印队列
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        # 如果打印机空闲且有打印队列中有作业
        if (not labprinter.busy()) and (not printQueue.is_empty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        # 打印机进行一秒
        labprinter.tick()
    # 计算平均等待时间以及是否还有任务未完成
    average_wait = sum(waitingtimes) / len(waitingtimes)
    print('Average waitting time is %6.2f. Tasks last: %d'
          %(average_wait,printQueue.size()))

for i in range(20):
    simulation(3600,5)
