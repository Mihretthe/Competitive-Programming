from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import factorial

def comb(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def solve():
    n = I()

    print(comb(n, 5) + comb(n, 6) + comb(n, 7))

 
 
 
 
T = 1
for _ in range(T):
    solve()