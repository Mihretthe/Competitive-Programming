from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    matrix = []
    for _ in range(n):
        row = list(S())
        matrix.append(row)
    
    row_prefix = [[0 for _ in range(m + 1)] for j in range(n + 1)]
    col_prefix = [[0 for _ in range(m + 1)] for j in range(n + 1)]
    
    
        
        
    
 
 
 
 
T = 1
for _ in range(T):
    solve()