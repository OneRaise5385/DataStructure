from structures import StackEnd

# 十进制转化为二进制
def divide_2(dec_number):
    remstack = StackEnd()
    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2
    binstring = ''
    while not remstack.is_empty():
        binstring += str(remstack.pop())
    return binstring

print('十进制转化为二进制测试: ' + divide_2(3))

# 十进制向十六进制一下的任意进制转换
def divide_any(dec_number,base):
    anystack = StackEnd()
    while dec_number > 0:
        rem = dec_number % base
        anystack.push(rem)
        dec_number = dec_number // base
    anystring = ''
    digits = '0123456789ABCDEF'
    while not anystack.is_empty():
        anystring += digits[anystack.pop()]
    return anystring

print('任意进制转换测试：' + divide_any(10,16))

    