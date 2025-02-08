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
    a = IL()
    counter = Counter(a)

    n = len(counter)
    ans = 1

    for i in range(1, n + 1):
        ans *= i 

    print(ans)

 
 
 
T = 1
for _ in range(T):
    solve()