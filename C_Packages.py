from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import sqrt


def solve():
    n, k = II()


    
    factors = set()

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    maxi = 1

    for i in factors:
        if i <= k:
            maxi = max(maxi, i)
    
    print(n//maxi)
    

 
 
 
 
T = I()
for _ in range(T):
    solve()