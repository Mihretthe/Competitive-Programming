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

    first = sum(a[:-2])
    first = a[-2] - first
    first = a[-1] - first
    print(first)
 
 
 
 
T = I()
for _ in range(T):
    solve()