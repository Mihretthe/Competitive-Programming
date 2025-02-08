from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():

    n, k = II()
    
    if n == 1 and k == 10:
        print(-1)
        return
    
    ans = 1
    ans *= (10 ** (n - 1))
    
    MOD = ans % k
    
    if MOD == 0:
        print(ans)
    else:
        print(ans + (k - MOD))
 
 
 
 
T = 1
for _ in range(T):
    solve()