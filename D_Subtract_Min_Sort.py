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
    
    for i in range(n - 1):
        mini = min(a[i], a[i + 1])
        if mini == a[i + 1] and mini != a[i]:
            print("NO")
            return
        a[i] -= mini
        a[i + 1] -= mini
    print("YES")
 
 
 
 
T = I()
for _ in range(T):
    solve()