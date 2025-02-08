from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n, b, c = II()
    count = 0
    
    if b == 0:
        if c < n:
            if c == n - 1 or c == n - 2:
                print(n - 1)
            else:
                print(-1)
        else:
            print(n)
    else:
        if n == 1:
            if c == 0:
                print(0)
            else:
                print(1)
            return 
        calc = (n - c) / b
        if calc == int(calc):  
            calc = int(calc)
        else:
            calc = ceil(calc)
        if calc < 0:
            print(n)
        else:
            print(n - calc)



 
 
 
 
T = I()
for _ in range(T):
    solve()