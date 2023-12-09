s = input()
if s[0] in "ah":
    if s[1] in "18":
        print(3)
    else:
        print(5)
else:
    if s[1] in "18":
        print(5)
    else:
        print(8)