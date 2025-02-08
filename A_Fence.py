from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf

def solve():
    n, k = II()

    h = IL()

    prefix = [0]

    for i in range(n):
        prefix.append(prefix[-1] + h[i])
    
    index = -1
    mini = inf


    for i in range(k, n + 1):
        if prefix[i] - prefix[i - k] < mini:
            index = i - k + 1
            mini = prefix[i] - prefix[i - k]
    
    print(index)

 
 
 
T = 1
for _ in range(T):
    solve()