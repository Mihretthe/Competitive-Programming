from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():

    s = S()
    n = len(s)
    if s[:n//2] == s[n//2:]:
        print("YES")
    else:
        print("NO")
 
 
 
 
T = I()
for _ in range(T):
    solve()