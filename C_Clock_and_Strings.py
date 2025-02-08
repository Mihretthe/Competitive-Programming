from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    a, b, c, d = II()
    first = sorted([a, b])
    second = sorted([c, d])

    a, b = first
    c, d = second

    if c in range(a, b + 1) and d in range(a, b + 1):
        print("NO")
    elif c not in range(a, b + 1) and d not in range(a, b + 1):
        print("NO")
    else:
        print("YES")
    
        

   
 
 
 
T = I()
for _ in range(T):
    solve()