
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter

from bisect import bisect_right, bisect_left


 
def solve():
    n, k = II()
    a = IL()
    left = min(a) - 1e-7
    right = max(a) 
    
    while right -left > 1e-7:
        mid = (right + left) / 2
        zero = 0
        for i in a:
            if i > mid:
                zero += (i - mid) - (i - mid)*(k/100)
            else:
                zero -= (mid - i)
        
        if zero >= 0:
            left = mid 
        else:
            right = mid 

    print(right)

        



    

T = 1
for _ in range(T):
    solve()