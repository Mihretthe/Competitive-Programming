s = input()

if s[0] == "4":
    n = 1
else:
    n = 2

for i in s[1:]:
    if i == "4":
        n = (2 * n) + 1
    else:
        n = (2 * n) + 2

print(n)
