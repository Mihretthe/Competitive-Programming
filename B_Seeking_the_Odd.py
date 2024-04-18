from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import log

def solve():
    n = I()
    ll = log(n, 2)
    if int(ll) == ll:
        print("NO")
    else:
        print("YES")


T = I()
for _ in range(T):
    solve()