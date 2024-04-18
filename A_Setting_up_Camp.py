def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
 
def solve():
    a, b, c = II()
    remain = (3 - (b % 3)) % 3
    if c < remain:
        print(-1)
        return 

    print(a + ceil((b + c)/ 3))
 
 
 
T = I()
for _ in range(T):
    solve()