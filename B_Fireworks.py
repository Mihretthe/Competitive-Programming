def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
 
def solve():
    a, b, m = II()
    print(m // b + m // a + 2)
 
 
 
T = I()
for _ in range(T):
    solve()