from structures import StackEnd

# 简单括号匹配问题
def per_match_easy(symbol_string):
    s = StackEnd()
    judge = True
    for i in symbol_string:
        if i == '(':
            s.push(i)
        else:
            if s.is_empty():
                judge = False
            else:
                s.pop()

    if judge and s.is_empty():
        return True
    else:
        return False

# 通用括号匹配算法
def per_match(symbol_string):
    s = StackEnd()
    judge = True
    for i in symbol_string:
        if i in '[{()}]':
            if i in '[{(':
                s.push(i)
            else:
                if s.is_empty():
                    judge = False
                else:
                    s.pop()
    if judge and s.is_empty():
        return True
    else:
        return False

print('简单匹配测试')
print(per_match_easy('((()))'))
print('通用匹配测试')
print(per_match('(sfsf{[]})'))

