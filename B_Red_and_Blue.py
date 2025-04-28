from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

"""
6 1 8 5
2 5 1

10 7 9 11
1 2

"""

def solve():
    n = I() + 1
    a = [0] + IL()
    m = I() + 1
    b = [0] + IL()
    
    
    for i in range(1, n):
        a[i] += a[i - 1]
    
    
    for i in range(1, m):
        b[i] += b[i - 1]
    
    print(max(a) + max(b))
 
 
 
 
T = I()
for _ in range(T):
    solve()