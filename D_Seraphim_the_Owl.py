def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil

 
def solve():
    n, m = II()
    a = IL()
    b = IL()
    pre_calc = 0
    ans = float('inf')


    for i in range(n - 1,-1, -1):
        if i < m:
            ans = min(ans, pre_calc + a[i])
        pre_calc += (min(a[i], b[i]))
        
        

    print(ans)
 
 
 
T = I()
for _ in range(T):
    solve()