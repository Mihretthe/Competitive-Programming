from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m, q = II()

    a = IL()
    b = I()

    maxi = max(a)
    mini = min(a)

    if b < mini:
        print(mini - 1)
    elif b > maxi:
        print(n - maxi)
    else:
        print((maxi - mini) // 2)
 
 
 
 
T = I()
for _ in range(T):
    solve()