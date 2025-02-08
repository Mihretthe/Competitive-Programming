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
    b = IL()

    for i in range(n):
        mini = min(a[i], b[i])
        maxi = max(a[i], b[i])
        a[i] = mini
        b[i] = maxi
    
    
    print(max(a) * max(b))
 
 
 
 
T = I()
for _ in range(T):
    solve()