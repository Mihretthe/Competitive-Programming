def helpMath(s):
    s = s.split("+")
    s.sort()
    s = "+".join(s)
    return s
print(helpMath(input()))
