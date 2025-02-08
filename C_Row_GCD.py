from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd, lcm

def calc(a, b):
    return gcd(a, b) == gcd(a+b, a)

def solve():
    n, m = II()
    a = IL()
    b = IL()

    gc = a[0]

    """
    gcd(a, b) = gcd(a+b, a)
    """

    for i in range(1, n):
        gc = gcd(gc, a[i])


    


    
    

 
 
 
 
T = 1
for _ in range(T):
    solve()