from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()
    x = 0
    for i in range(n):
        if "+" in S():
            x += 1
        else:
            x -= 1
    print(x)
 
 
 
T = 1
for _ in range(T):
    solve()