from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_right

def solve():
    n = I()
    a = IL()
    
    a = [(a[i], i) for i in range(n)]
    a.sort()
    print(a)
    
    prefix = [a[0][0]]
    
    for i in range(1, n):
        prefix.append(prefix[-1] + a[i][0])
        
    
    
 
 
 
T = I()
for _ in range(T):
    solve()