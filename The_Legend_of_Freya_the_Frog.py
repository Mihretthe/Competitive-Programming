from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    x, y, k = II()
    if x > y and ceil(x / k) != ceil(y / k):
        print(ceil(x / k) * 2 - 1)
    else:
        print(ceil(y / k) * 2)
 
 
 
T = I()
for _ in range(T):
    solve()