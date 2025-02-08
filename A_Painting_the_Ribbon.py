from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m, k = II()
    if (n + m - 1) / m + k >= n:
        print("NO")
    else:
        print("YES")
 
 
 
T = I()
for _ in range(T):
    solve()