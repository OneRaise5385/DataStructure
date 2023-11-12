import turtle
t = turtle.Turtle()

def listsum(numlist):
    '''列表元素加和'''
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])
    
list1 = [1,3,4,5]
a = listsum(list1)
print(a)

def tostr(n,base):
    '''进制的转换'''
    converstring = '0123456789ABCDEF'
    if n < base:
        return converstring[n]
    else:
        return tostr(n//base,base) + converstring[n%base]
    
num1 = 41
b = tostr(num1,10)
c = tostr(num1,2)
d = tostr(num1,16)
print(b)
print(c)
print(d)

def drawspiral(t,linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawspiral(t,linelen-5)

drawspiral(t,100)
turtle.done()