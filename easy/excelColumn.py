'''
168. Excel Sheet Column Title

Given an integer `columnNumber`, return its corresponding column title as it appears in an excel sheet.
'''

def convertToTitle(columnNumber):
    output = ""
    
    while columnNumber > 0:
        output = chr(ord("A") + (columnNumber - 1) % 26) + output
        columnNumber = (columnNumber - 1) // 26

    return output

print(convertToTitle(32))
