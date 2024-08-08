def longestCommonPrefix(strs):
    l = len(strs)
    prefix = ""
    found = {}

    for i in zip(*strs):
        if len(set(i)) == 1:
            prefix += i[0]
        else:
            return prefix

    
    return prefix

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["aggregate", "aggravate", "agriculture"]))
