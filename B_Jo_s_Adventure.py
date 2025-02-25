from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    nums = IL()
    
    prefix = [0]
    suffix = [0] * n
    
    for i in range(1, n):
        prefix.append(prefix[-1])
        if nums[i] < nums[i - 1]:
            prefix[-1] +=  nums[i - 1] - nums[i]
            
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            suffix[i] = (nums[i + 1] - nums[i])
        suffix[i] += suffix[i + 1]
        
        
    # print(suffix)
            
        
    
    for _ in range(m):
        s, t = II()
        if s < t:
            print(prefix[t - 1] - prefix[s - 1])
        else:
            print(suffix[t - 1] - suffix[s - 1])
        
 
 
 
 
T = 1
for _ in range(T):
    solve()