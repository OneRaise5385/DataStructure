from structures import Queue

def hot_potato(name_list,num):
    '''约瑟夫问题'''
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

a = hot_potato(['Bill','David','Susan','Jane','Kent','Brad'],2)  # 建立n个人的list
print(a)