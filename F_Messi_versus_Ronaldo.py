from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    a = IL()
    ans = 0

    for j in range(n):
        andy = 0
        for i in range(n):
            andy += (a[i] & a[j])
        orr = 0 
        for k in range(n):
            orr += (a[k] | a[j])
        ans += (andy * orr)
    print(ans % 1000000007)
        
 
 
 
 
T = I()
for _ in range(T):
    solve()