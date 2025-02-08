from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from math import inf


def solve():
    n, s = II()
    a = IL()
    
    def check(mid):
        if mid == 0:
            return 0
        
        answer = []
        
        for i in range(n):
            answer.append((i + 1) * mid + a[i])
        
        answer.sort()
        
        return sum(answer[:mid])
    
    left = 0
    right = n
    
    
    
    while left <= right:
        mid = (left + right) // 2
        
        if check(mid) <= s:
            left = mid + 1
        else:
            right = mid - 1
        
   
    
    print(right,check(right))
    
    
    
 
T = 1
for _ in range(T):
    solve()