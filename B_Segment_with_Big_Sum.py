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
    nums = IL()

    left = 0
    min_length = inf
    total = 0
    for right in range(n):
        total += nums[right]

        while total >= k:
            min_length = min(min_length, right - left + 1)
            total -= nums[left]
            left += 1

        
    if min_length == inf:
        print(-1)
        return
    print(min_length)
 
 
 
 
T = 1
for _ in range(T):
    solve()