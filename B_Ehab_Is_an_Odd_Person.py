from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n = I()
    a = IL()

    evens = 0
    odds = 0

    for i in range(n):
        if a[i] % 2:
            odds += 1
        else:
            evens += 1

    if not evens or not odds:
        print(*a)
    else:
        print(*sorted(a))
    
    


 
 
 
T = 1
for _ in range(T):
    solve()