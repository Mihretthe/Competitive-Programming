def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
    

def solve():
    a, b = II()
    if a == b:
        print(a)
    else:
        print(1)
    
    
T = 1
for _ in range(T):   
    solve()
    