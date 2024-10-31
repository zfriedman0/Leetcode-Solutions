'''
7. Reverse Integer

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2^31, 2^31-1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

def reverse(x):
    if x < 0:
        x = str(-x)
        x = x[::-1]
        x = -int(x)
    else:
        x = str(x)
        x = x[::-1]
        x = int(x)

    if x < (-2)**31 or x > (2**31)-1:
        return 0

    return x

print(reverse(-123))
