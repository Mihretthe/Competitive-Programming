from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n = I()
    a = IL()
    a.sort()
    
    first = (a[0] + a[1]) // 2

    for i in range(2, n):
        first = (first + a[i]) // 2
    
    print(first)


 
 
 
T = I()
for _ in range(T):
    solve()