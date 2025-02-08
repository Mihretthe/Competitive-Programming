from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd
from collections import defaultdict

def solve():
    n = I()
    a = IL()

    dp = defaultdict(list)
    maxi = 1

    for j in range(n):
        num = a[j]
        for i in dp:
            if gcd(num, dp[i][-1]) > 1 and num > i:
                dp[i].append(num)
            maxi = max(maxi, len(dp[i]))  
        dp[j] = [num]

    values = [len(i) for i in dp.values()]
    
    values.sort()
    print(values[-1])
 
 
 
T = 1
for _ in range(T):
    solve()