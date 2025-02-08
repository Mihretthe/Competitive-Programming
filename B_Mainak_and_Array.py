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
    
    maxi = max(max(a) - a[0], a[-1] - min(a), a[n - 1] - a[0])

    for i in range(n - 1):
        maxi = max(maxi, a[i] - a[i + 1])
        
    print(maxi)

 
 
T = I()
for _ in range(T):
    solve()