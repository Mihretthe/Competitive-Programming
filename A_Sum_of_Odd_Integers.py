from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n, k = II()
    
    """
    1 = 1
    1 + 3 = 4
    1 + 3 + 5 = 9
    1 + 3 + 5 + 7 = 16
    1 + 3 + 5 + 7 + 9 = 25
    1 + 3 + 5 + 7 + 9 + 11 = 36
    1 + 3 + 5 + 7 + 9 + 11 + 13 = 49
    1 + 3 + 5 + 7 + 9 + 11 + 13 + 17 = 63
    ...    
   
    
    
    """
    
    if n % 2 and k % 2 == 0 or n % 2 == 0 and k % 2:
        print("NO")
        return 
    
    
    
    if n >= k * k:
        print("YES")
    else:
        print("NO")
 
 
 
T = I()
for _ in range(T):
    solve()