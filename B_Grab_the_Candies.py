
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
    

def solve():
    n = I()
    a = IL()
    evens = 0
    odds = 0

    for num in a:
        if num % 2:
            odds += num
        else:
            evens += num

    if evens > odds:
        print("YES")
    else:
        print("NO")
    
    
    
T = I()
for _ in range(T):   
    solve()
    