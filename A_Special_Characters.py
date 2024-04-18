def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    n = I()
    if n % 2:
        print("NO")
    else:
        print("YES")
        ans = []
        for i in range(n // 2):
            for j in range(2):
                ans.append("AB"[i & 1])
        print(''.join(ans))




    
 
T = I()
for _ in range(T):   
    solve()

    