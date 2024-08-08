l1 = [2,4,3]
l2 = [5,6,4]

def add_two(l1, l2):
    l1.reverse()
    l2.reverse()
    
    n1 = int(''.join(str(x) for x in l1))
    n2 = int(''.join(str(x) for x in l2))

    tot = str(n1 + n2)

    tot = list(digit for digit in tot)

    tot.reverse()

    return tot

print(add_two(l1, l2))
        
