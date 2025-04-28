from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, x = II()
    a = IL()
    
    total = sum(a)
    
    if total / n == x:
        print("YES")
    else:
        print("NO")
 
 
 
 
T = I()
for _ in range(T):
    solve()