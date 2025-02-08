from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    m, a, b, c = II()
    first = m
    second = m

    first = max(0, first - a)
    second = max(0, second - b)
    aseated = m - first
    bseated = m - second

    remain = first + second

    cseated = min(c, remain)
 
 
    print(aseated + bseated + cseated)
 
T = I()
for _ in range(T):
    solve()