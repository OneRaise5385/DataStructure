from structures import StackEnd

def infix_to_postfix(infixexpr):
    '''中缀表达式转后缀表达式通用算法'''
    # 设置优先级
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    token_list = []
    for i in infixexpr:
        if i != ' ':
            token_list.append(i)
    opstack = StackEnd()
    postfix_list = []
    for token in token_list:
        # 操作数加入列表中
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            postfix_list.append(token)
        # 遇见括号压入栈中
        elif token in '(':
            opstack.push(token)
        # 遇见括号先弹出括号里的操作符
        elif token in ')':
            toptoken = opstack.pop()
            while toptoken != '(':
                postfix_list.append(toptoken)
                toptoken = opstack.pop()
        # 操作运算符压入栈中
        elif token in '+-*/':
            # 后来的运算符的优先级
            while opstack.size() > 0 and prec[token] <= prec[opstack.peek()]:
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while opstack.size() > 0:
        postfix_list.append(opstack.pop())
    return postfix_list

print(infix_to_postfix('A+B*C'))
print(infix_to_postfix('(A+B)*C'))

def postfix_eval(postfix_list):
    operandstack = StackEnd()
    for token in postfix_list:
        if token in '0123456789':
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = domath(token,operand1,operand2)
            operandstack.push(result)
    return operandstack.pop()

def domath(op,op1,op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2

a = '(2+3)*5'
b = infix_to_postfix(a)
c = postfix_eval(b)
print(b)
print(c)