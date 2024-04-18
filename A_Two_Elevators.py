from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    a, b, c = II()
    a = abs(a - 1)
    if c > b:
        b = abs(c - b + c - 1 )
    else:
        b = abs(b - 1)
    
    # print(a, b)
    if a == b:
        print(3)
    elif a < b:
        print(1)
    else:
        print(2)
 
 
 
 
T = I()
for _ in range(T):
    solve()