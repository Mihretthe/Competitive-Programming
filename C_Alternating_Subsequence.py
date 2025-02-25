from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf

def solve():
    n = I()
    nums = IL()
    
    ans = 0
    max_val = float('-inf')
    
    for i in range(n-1):
        max_val = max(max_val, nums[i])
        # check if alternation
        if (nums[i] > 0 and nums[i+1] < 0 ) or (nums[i] < 0 and nums[i+1] > 0):
            ans += max_val
            max_val = nums[i+1]
    max_val = max(max_val, nums[-1])
    ans += max_val
    print(ans)
            
            
                
            
            
        
 
 
 
 
T = I()
for _ in range(T):
    solve()