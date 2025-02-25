from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter
from random import randint


def solve():
    xor = randint(1, 100)
    n, k = II()
    nums = IL()
    
    nums = [num ^ xor for num in nums]
    
    
    
    counter = Counter(nums)

    collect = []
    
    for key, val in counter.items():
        if val >= k:
            collect.append(key ^ xor)
    
    if not collect:
        print(-1)
        return
    
    
    collect.sort()
    
    ans = []
    
    left = 0
    
    # print(collect)
    
    for right in range(len(collect)):        
        
        while left < right and collect[right] - collect[left] != right - left:
            left += 1
        
        ans.append((collect[left], collect[right]))
    
    # print(ans)
    
    ans.sort(key = lambda x : x[1] - x[0])
    print(*ans[-1])
            
            
    
                
            
 
 
 
 
T = I()
for _ in range(T):
    solve()