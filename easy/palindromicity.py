def palindromic(x):
    pal = False

    x = list(''.join(num for num in str(x)))
    y = x[::-1]
    
    if x == y:
        pal = True

    return pal

print(palindromic(9989))
