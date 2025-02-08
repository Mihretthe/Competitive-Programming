from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict
def solve():
    ans = defaultdict(int)
    ans[1] = 400
    ans[2] = 300
    ans[3] = 200
    ans[4] = 150
    ans[5] = 100
 
    n, m = II()
    print(ans[n] + ans[m])
 
T = I()
for _ in range(T):
    solve()