from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd

def solve():
    a, b = II()
    if gcd(a, b) == 1:
        print("Finite")
    else:
        print("Infinite")
 
 
 
T = I()
for _ in range(T):
    solve()