from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    a, b = II()
    counter = defaultdict(int)
    for i in range(1, 7):
        if abs(a - i) < abs(b - i):
            counter[a] += 1
        elif abs(a - i) > abs(b - i):
            counter[b] += 1
        else:
            counter["draw"] += 1
    
    print(counter[a], counter["draw"], counter[b])

 
T = 1
for _ in range(T):
    solve()