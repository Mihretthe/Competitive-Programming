def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    n, m = II()
    s = input()
    w = input()

    letters = "abcdefghijklmnopqrstuvwxyz"
    
    check = 0

    for i in range(m):
        check += letters.index(w[i])

    total = 0

    for i in range(m):
        total += letters.index(s[i])
    
    if total == check:
        print("YES")
        return 
    
    for i in range(1, n - m + 1):
        total -= letters.index(s[i - 1])
        total += letters.index(s[i + m - 1])
        if total == check:
            print("YES")
            break
    else:
        print("NO")
    
    
 
T = I()
for _ in range(T):
    solve()