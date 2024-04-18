def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil

 
def solve():
    n = I()
    a = list(map(int, list(input())))

    pre_zeros = [0]
    pre_ones = [0]
    

    for i in range(n):
        if a[i] == 0:
            pre_zeros.append(pre_zeros[-1] + 1)
            pre_ones.append(pre_ones[-1])
        else:
            pre_ones.append(pre_ones[-1] + a[i])
            pre_zeros.append(pre_zeros[-1])
   
    ans = float('inf')
    if pre_ones[-1] >= ceil(n / 2):
        ans = 0
    for i in range(n + 1):
        if ceil((i) / 2) <= pre_zeros[i] and ceil((n - i) / 2) <= (pre_ones[-1] - pre_ones[i]):
            
            
            if abs(n / 2 - i) < abs(n / 2 - ans):
                ans = i
    
    print(ans)
 
 
 
T = I()
for _ in range(T):
    solve()