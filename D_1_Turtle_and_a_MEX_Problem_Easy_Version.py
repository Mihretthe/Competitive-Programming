from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    tot = 0
    for_next = []
    for _ in range(n):
        a = IL()
        l = a[0]
        a = sorted(a[1:] + for_next)
        
    ans = m * (m + 1) // 2
    print(ans + tot)

 
 
 
 
T = I()
for _ in range(T):
    solve()