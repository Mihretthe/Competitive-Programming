
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter

from bisect import bisect_right, bisect_left
 
def solve():
    s, b = II()
    a = IL()

    bases = []
    power = []


    for _ in range(b):
        bases.append(tuple(II()))
    
    bases.sort()

    golds = [0]

    for d, g in bases:
        power.append(d)
        golds.append(golds[-1] + g)

    ans = []
    power.sort()

    for space in a:
        index = bisect_right(power, space)
        ans.append(golds[index])
    print(*ans)
    

T = 1
for _ in range(T):
    solve()