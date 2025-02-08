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

    ans = a[0]

    for i in range(1, n):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]
    
    print(ans)
 
 
T = I()
for _ in range(T):
    solve()