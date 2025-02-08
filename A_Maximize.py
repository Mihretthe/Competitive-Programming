from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd, sqrt

def solve():
    x = I()
    maxi = 1
    for i in range(2,x):
        if gcd(maxi,x) <= gcd(i, x):
            maxi = i 
    print(maxi)


 
 
 
 
T = I()
for _ in range(T):
    solve()