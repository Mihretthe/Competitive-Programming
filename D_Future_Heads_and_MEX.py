from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter, defaultdict
from math import inf


def solve():
    n = I()
    a = IL()
    
    counter = defaultdict(int)
    
    for i in a:
        counter[i] += 1  
    
  
    mex = 0       

    for i in range(5001):
        if i not in counter:
            mex = i
            break
    
    # print(mex, keys)
    counter = {0: 2000, 1: 600, 2:1 }
    zero = counter[0]
    
    calc = inf
    for key, val in counter.items():
        num = (mex * (val - 1)) + (key * zero)
        calc = min(calc, num)
        print(key, num)
        
        
    print(calc)
            
    
T = I()
for _ in range(T):
    solve()