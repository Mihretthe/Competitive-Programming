from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    s = S()
    counter = defaultdict(int)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            counter[s[i:j]] += 1

    maxi = 0

    for key, value in counter.items():
        if value >= 2:
            maxi = max(maxi, len(key))

    print(maxi)
 
 
 
 
T = 1
for _ in range(T):
    solve()