from math import inf
from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict 

def calc(s, n, even, odd):
    
    # print(s, n)
    for i in range(n):
        if i % 2:
            even[s[i]] += 1
        else:
            odd[s[i]] += 1
    
    max_e = max(even.values())
    max_o = max(odd.values())

    # print(max_e ,max_o)
    return ((n // 2 - max_e) + (n // 2 - max_o) )

def solve():
    n = I()
    s = S()
    if n % 2:
        if n == 1:
            print(1)
            return
        
        def dp(already, index, even, odd):
            if index == n:
                return (even, odd)
            if already:
                if (index - 1) % 2:
                    even[s[index]] += 1
                else:
                    odd[s[index]] += 1
                return dp(already, index + 1, even, odd)
            else:
                return dp(not already, index + 1, even, odd)
            
        even, odd = (dp(False, 0, defaultdict(int), defaultdict(int)))
        print(calc(s, n - 1, even, odd) + 1)
            
                
    else:
        print(calc(s, n, defaultdict(int), defaultdict(int)))
 
 
 
 
T = I()
for _ in range(T):
    solve()