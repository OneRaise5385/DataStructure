import turtle
def tree(branchlen):
    '''分形树'''
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen - 15)
        t.left(40)
        tree(branchlen - 15)
        t.right(20)
        t.backward(branchlen)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()
