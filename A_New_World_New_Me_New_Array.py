from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n, k, p = II()
    if (k / n) > p or (k / n) < -p:
        print(-1)
        return
    
    print(ceil(abs(k)/p))
 
 
 
T = I()
for _ in range(T):
    solve()