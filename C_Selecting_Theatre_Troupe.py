from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import factorial

def numOfComb(num, r):
    fac_num = factorial(num)
    fac_r = factorial(r)

    return fac_num // (fac_r * factorial(num - r))


def solve():
    n, m, t = II()
    ans = 0

    for i in range(4, t):
        ans += numOfComb(t, i)
    
    print(ans)

 
 
 
 
T = 1
for _ in range(T):
    solve()