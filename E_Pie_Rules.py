from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heapify, heappop, heappush

def solve():
    n = I()
    a = IL()
    a.sort()
    
    alice = 0
    bob = a[0]
    
    for i in range(1, n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
 
    print(alice, bob)
T = 1
for _ in range(T):
    solve()