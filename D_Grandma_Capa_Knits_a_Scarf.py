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
    s = S()
    
     
    
    my_set = set(s)
    mini = inf
    
    for letter in my_set:
        left = 0
        right = n - 1
        count = 0
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif letter == s[left]:
                left += 1
                count += 1
            elif letter == s[right]:
                right -= 1
                count += 1
            else:
                break
        else:
            mini = min(mini, count)
    
    if mini != inf:
        print(mini)
    else:
        print(-1)
                
                
        
        
 
 
 
 
T = I()
for _ in range(T):
    solve()