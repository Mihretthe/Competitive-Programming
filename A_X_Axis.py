from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    x, y, z = II()

    mini = abs(x - y) + abs(x - z)
    mini = min(mini, abs(x - y) + abs(y - z))
    mini = min(mini, abs(z - y) + abs(x - z))
 
 
    print(mini)
 
T = I()
for _ in range(T):
    solve()