from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf
from bisect import bisect_left

def calc(x, y, z):
    return (x - y)**2 + (y - z)**2 + (x - z)**2


def solve():
    nr, ng, nb = II()
    r = SIL()
    g = SIL()
    b = SIL()
    
    def calculateMini(num, arr1, arr2):
        index1 = bisect_left(arr1, num)
        index2 = bisect_left(arr2, num)
        
        mini = inf
        
        index1 = bisect_left(arr1, num)
        candidate1 = [arr1[index1 - 1] if index1 > 0 else -inf, arr1[index1] if index1 < len(arr1) else inf]
        candidate2 = [arr2[index2 - 1] if index2 > 0 else -inf, arr2[index2] if index2 < len(arr2) else inf]
        
        
        for y in candidate1:
            for z in candidate2:
                mini = min(mini, calc(num, y, z))
            
        return mini
    
    mini = inf
    
    for i in r:
        mini = min(mini, calculateMini(i, g, b))
    
    for i in g:
        mini = min(mini, calculateMini(i, r, b))
    
    for i in b:
        mini = min(mini, calculateMini(i, g, r))
        
    
    print(mini)
        
    
    
    
    
    
 
 
 
T = I()
for _ in range(T):
    solve()