'''
67. Add Binary

Given two strings `a` and `b`, return their sum as a binary string.
'''

def addBinary(a, b):
    a_list = list(reversed([num for num in a]))
    b_list = list(reversed([num for num in b]))
    carry = False
    res = ""

    if len(a_list) < len(b_list):
        a_list.append('0')
    elif len(b_list) < len(a_list):
        b_list.append('0')

    for pair in list(zip(a_list, b_list)):
        if not carry:
            if pair == ('0', '0'):
                res += '0'
            elif pair == ('0', '1') or pair == ('1', '0'):
                carry = True
                res += '0'
            elif pair == ('1', '1'):
                res += '1'


    return res

print(addBinary("11", "1"))
