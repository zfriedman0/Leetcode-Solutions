def isValid(s):
    parenthesis = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in s:
        if char in parenthesis.values():
            stack.append(char)
        elif char in parenthesis.keys():
            if not stack or parenthesis[char] != stack.pop():
                return False
    
    return not stack

print(isValid('()['))

