from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd

def solve():
    increasing = False
    decreasing = False
    length, k = II()
    nums = IL()
    

    for i in range(length):
        if nums[i] > k:
            increasing = True
        elif nums[i] < k:
            decreasing = True
        
        if increasing and decreasing:
            print(-1)
            return 
        
    gcdi = abs((nums[0]) - k)

    for i in range(length):
        if nums[i] != k:
            gcdi = gcd(gcdi, abs(nums[i] - k))

    answer = 0
    for i in range(length):
        if gcdi:
            answer += abs((nums[i] - k)) // gcdi - 1
    
    print(answer)
 
 
T = I()
for _ in range(T):
    solve()