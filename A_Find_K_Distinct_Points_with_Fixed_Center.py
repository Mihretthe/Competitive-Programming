from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    x, y, k = II()
    xx = 0
    yy = 0
    if k == 1:
        print(x, y)
        return
    if k % 2:
        print(x, y)
    for i in range(1, k // 2 + 1):
        print(x - i, y)
        print(x + i, y)
        
 
 
 
 
T = I()
for _ in range(T):
    solve()