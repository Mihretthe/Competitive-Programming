from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    x, y, k = II()
    mini = min(x, y)
    print(f"0 0 {mini} {mini}")
    print(f"0 {mini} {mini} 0")
    
 
 
 
 
T = I()
for _ in range(T):
    solve()