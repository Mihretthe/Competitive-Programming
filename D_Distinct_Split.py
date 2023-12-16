from collections import defaultdict

t = int(input())

def counter(string):
    return len(set(string))

for _ in range(t):
    n = int(input())
    s = input()
   
    count = 0

    for i in range(1,n):
        a = s[:i]
        b = s[i:]
        c = counter(a) + counter(b)
        count = max(count, c)

    print(count)



    