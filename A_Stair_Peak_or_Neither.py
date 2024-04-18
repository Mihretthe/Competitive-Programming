
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from collections import defaultdict
    

def solve():
    a, b, c = II()

    if a < b and b < c:
        print("STAIR")
    elif a < b and b > c:
        print("PEAK")
    else:
        print("NONE")

    

    
    
    
    
T = I()
for _ in range(T):   
    solve()
    