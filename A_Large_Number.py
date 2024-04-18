
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter
 
def solve():
    n, d = II()
    num = input()

    for i in range(n):
        if int(num[i]) < d:
            num = num[:i] + str(d) + num[i:]
            break
    else:
        num += str(d)
    
    print(num)
 
 
T = I()
for _ in range(T):
    solve()