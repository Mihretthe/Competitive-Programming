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

    ans = max(a[:2]) - 1

    for i in range(1, n):
        maxx = max(a[i], a[i - 1])
        if ans >= maxx:
            ans = maxx - 1
    
    print(ans)


 
 
 
 
T = I()
for _ in range(T):
    solve()