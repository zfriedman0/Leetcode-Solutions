def romanToInt(s):
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0

    for i, char in enumerate(s):
        if i + 1 < len(s) and mapping[s[i+1]] > mapping[s[i]]:
            total -= mapping[s[i]]
        else:
            total += mapping[s[i]]

    return total

print(romanToInt("CCLXX"))
