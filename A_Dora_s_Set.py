from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    l, r = II()
    
    odd = 0
    even = 0

    for i in range(l, r + 1):
        if i % 2:
            odd += 1
        

    print(odd // 2)
        

 
 
 
 
T = I()
for _ in range(T):
    solve()