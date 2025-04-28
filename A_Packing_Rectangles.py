from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    w, h, n = II()
    
    def check(mid):
        width = min(mid, (mid // w) * w)
        height = min(mid, (mid // h) * h)
        return width * height >= n * w * h
    
    
    low = 0
    high = 10**27
    
    
    while low <= high:
        mid = (low + high) // 2
        
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
    
    print(low)
        
 
 
 
T = 1
for _ in range(T):
    solve()