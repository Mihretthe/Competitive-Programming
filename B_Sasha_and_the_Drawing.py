def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil

def same(n,k):
    return k <= (2*n - 2) * 2
 
def solve():
    n, k = II()

    if same(n,k):
        print((k + 1) // 2)
    else:
        print((k // 2) + 1)
        
 
T = I()
for _ in range(T):
    solve()