from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, x, y = II()
    
    def check(mid):
        
        num = mid // x + mid // y
        return num >= (n - 1)

    low = 0
    high = 2 * 10**9 + 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
        
    print(low + min(x, y))
            
    
    
    
 
 
 
 
T = 1
for _ in range(T):
    solve()