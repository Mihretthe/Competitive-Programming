from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n = I()

    if n % 3 == 0:
        print(n // 3)
    elif n % 3 == 1:
        if n == 1:
            print(2)
        else:
            n -= 4
            print(n // 3 + 2)

    else:
        print(n // 3 + 1)

    
 
 
 
 
T = I()
for _ in range(T):
    solve()