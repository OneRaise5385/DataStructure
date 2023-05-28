class StackEnd():
    '''栈抽象数据类型-栈顶尾端'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
class StackHead():
    '''栈抽象数据类型-栈顶首端'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)
    
    def peek(self):
        return self.items(0)
    
    def size(self):
        return len(self.items)

class Queue():
    '''队列-首段加入，尾端删除'''
    def __init__(self):
        self.items = []

    def items(self):
        return self.items

    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Deque():
    '''双端队列'''
    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
class Node():
    '''节点Node'''
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList():
    '''无序表的链接表实现-UnorderList'''
    def __init__(self):
        self.head = None

    def all(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class OrderedList():
    '''有序表的实现'''
    def __init__(self):
        self.head = None
        