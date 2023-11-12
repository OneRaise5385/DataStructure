from structures import Deque

def pelchecker(string):
    '''回文数的判定'''
    chardeque = Deque()
    for ch in string:
        chardeque.addRear(ch)
    stillequal = True
    while chardeque.size() > 1 and stillequal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillequal = False
    return stillequal

a = 'zhangyiju'
b = 'oppo'
c = 'radar'
print(pelchecker(a))
print(pelchecker(b))
print(pelchecker(c))
