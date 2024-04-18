
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
    

def solve():
    a, b, c = II()
    if a + b == c:
        print("+")
    else:
        print("-")
    
    
    
T = I()
for _ in range(T):   
    solve()
    