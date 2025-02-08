from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n, k = II()
    a = IL()
    a.sort()
    ans = k
    till = 0

    should = ceil(k / n)

    for i in range(n):
        if should > a[i]:
            ans += 1
        
        

    print(ans)
        
 

T = I()
for _ in range(T):
    solve()