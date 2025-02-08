from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n, k = II()
    s = S()
    
    if n == 2*k:
        print("NO")
        return
    
    left = 0
    

    while left < k:
        if s[left] == s[n - 1 - left]:
            left += 1
        else:
            print("NO")
            break
    else:
        print("YES")  

    
 
 
 
 
T = I()
for _ in range(T):
    solve()