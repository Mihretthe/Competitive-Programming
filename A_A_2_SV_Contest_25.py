from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    a, b, c, d = II()
    m = max(3*a / 10, a - (a/250 * c))
    v = max(3*b / 10, b - (b/250 * d))

    if m == v:
        print("Tie")
    elif m < v:
        print("Vasya")
    else:
        print("Misha")
 
 
 
T = 1
for _ in range(T):
    solve()