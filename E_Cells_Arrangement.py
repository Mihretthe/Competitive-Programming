from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    start = 1
    print(1, 1)
    for i in range(n - 1):
        start += 1
        print(start, 1)
        
    print()
 
 
 
T = I()
for _ in range(T):
    solve()