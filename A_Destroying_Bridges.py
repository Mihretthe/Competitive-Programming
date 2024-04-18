def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n, k = II()
    if k >= (n - 1):
        print(1)
    else:
        print(n)
 
 
 
T = I()
for _ in range(T):
    solve()