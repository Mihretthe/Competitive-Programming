from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, s = II()
    ans = 0
    while s > 0:
        ans += s // n
        s %= n
        n -= 1
    
    print(ans)
        
        
 
 
 
 
T = 1
for _ in range(T):
    solve()