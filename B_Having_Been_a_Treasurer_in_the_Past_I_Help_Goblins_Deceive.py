from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n = I()
    s = S()
    
    counter = Counter(s)
    
    hiphen = counter["-"]
    under = counter["_"]
    
    if hiphen % 2:
        first = hiphen // 2
        second = first + 1
        
        print(first * second * under)
    else:
        first = hiphen // 2
        print(first * first * under)
 
 
 
 
T = I()
for _ in range(T):
    solve()