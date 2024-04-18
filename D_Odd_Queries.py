from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    n, q = II()
    a = IL()

    prefix = [0]

    for i in range(n):
        prefix.append(prefix[-1] + a[i])
    
    total = prefix[-1]

    for i in range(q):
        l, r, k = II()

        if (total%2 - (prefix[r] - prefix[l - 1]) + ((k % 2) * (r - l + 1)% 2) )% 2:
            print("YES")
        else:
            print("NO")
    
    
    
T = I()
for _ in range(T):   
    solve()
    