from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from math import log2, ceil

def solve():
    n, k = II()
    
    
    if k % 2 == 0:    
        answer = [n - 1] * n
        answer[-2] = n 
    else:
        answer = [n] * n
        answer[-1] = n - 1
        
    print(*answer)
 
 
 
T = I()
for _ in range(T):
    solve()