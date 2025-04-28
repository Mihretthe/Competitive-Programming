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
    a = IL()

    counter = [0]
    memo = {}
    def recursive(num, target):
        if (num, target) in memo:
            return memo[(num, target)]
        counter[0] += 1
        if num <= target:
            final[0] = min(num, final[0])
            return 0
        
        if num % 2 == 0:
            memo[(num, target)] = 1 + 2 * recursive(num // 2, target) 
            return memo[(num, target)]

        memo[(num, target)] = 1 + recursive(num // 2 , target) + recursive((num // 2) + 1, target)
        return memo[(num, target)]
                   
    count = 0
    mini = a[-1]
    for i in range(n - 2, -1, -1):
        if a[i] > mini:
            final = [inf]
            count += recursive(a[i], mini)
            mini = final[0]
        else:
            mini = a[i]
    
    print(count)
    #  print(counter[0])
        
        
    
    
    
    
    
    
    
    
T = I()
for _ in range(T):
    solve()