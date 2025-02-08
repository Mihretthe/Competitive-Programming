from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import isqrt

def solve():
    n, k = II()
    array = []
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            array.append(i)
            if n // i != i:
                array.append(n // i)
    array.sort()
    
    if len(array) >= k:
        print(array[k - 1])
    else:
        print(-1)



 
 
 
 
T = 1
for _ in range(T):
    solve()