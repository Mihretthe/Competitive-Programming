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
    k = I()
    if len(s) < k:
        print("impossible")
        return 

    counter = Counter(s)

    print(max(0, k - len(counter)))



 
 
 
 
T = 1
for _ in range(T):
    solve()