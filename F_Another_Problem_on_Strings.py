from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def SLI() : return list(map(int, S()))

from collections import defaultdict

def solve():
    k = I()
    nums = SLI()
    
    previous = defaultdict(int)
    previous[0] = 1
    number = 0
    running_sum = 0
    
    for num in nums:
        running_sum += num
        number += previous[running_sum - k]
        previous[running_sum] += 1
    
    print(number)
        
    
    
 
 
 
 
T = 1
for _ in range(T):
    solve()