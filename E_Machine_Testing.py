def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
    

def solve():
    length = I()
    healths = IL()
    powers = IL()

    stack = [[float('inf'), powers[0]]]
    ans = 0

    for i in range(1, length):
        health = healths[i]
        power = powers[i]
        duration = 0
        
        while stack and health - ((stack[-1][0] - duration) * stack[-1][-1]) >= 0:            
            t, p = stack.pop()
            health -= (t - duration) * p
            duration += (t - duration)

        duration += ceil(health / stack[-1][-1])
        stack.append((duration, power))
        ans = max(ans, duration)
        
    print(ans)

            
T = I()
for _ in range(T):   
    solve()
    