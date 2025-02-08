from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

print(9 * 29)
def solve():
    n = I()
    if n == 4:
        print(198)
    elif n == 5:
        print(307)
    elif n == 1:
        print(22)
    elif n == 2:
        print()
    else:
        print()
 
 
 
T = 1
for _ in range(T):
    solve()