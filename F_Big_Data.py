from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import sqrt, isqrt, inf

def calc(a, b):
    return 2 * a + 2 * b

def solve():
    n = I()
    mini = inf
    

    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            mini = min(mini, calc(i, n // i))
    print(mini)


 
 
 
 
T = 1
for _ in range(T):
    solve()