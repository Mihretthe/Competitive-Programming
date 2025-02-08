from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

"""
T - erase minis
P - erase maxis
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush

def solve():
    n = I()
    a = IL()
    a.sort()
    if n % 2 == 0:
        print(max(a[n // 2 - 1], a[n//2]))
    else:
        print(a[n // 2])
    


 
 
 
 
T = I()
for _ in range(T):
    solve()