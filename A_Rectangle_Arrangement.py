from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = 0
    b = 0
    for _ in range(n):
        u, v = II()
        a = max(a, u)
        b = max(b, v)
    
    print(2*(a + b))
 
 
 
 
T = I()
for _ in range(T):
    solve()