def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)
 
def solve():
    n = I()
    if n % 3:
        print("First")
    else:
        print("Second")
 
 
 
 
T = I()
for _ in range(T):
    solve()