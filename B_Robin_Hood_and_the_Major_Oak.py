from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    
    if n % 2:
        odd = (k + 1) // 2
    else:
        odd = k // 2

    if odd % 2:
        print("NO")
    else:
        print("YES")
 
 
T = I()
for _ in range(T): 
    solve()