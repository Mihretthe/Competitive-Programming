from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    n, k = II()
    array = []
    
    for _ in range(n):
        num = I()
        array.append(num)
        
    def check(mid):
        count = 0
        for num in array:
            count += (num // mid)
        
        return count >= k
    
    low = 0
    high = max(array)
    
    while low <= high:
        mid = (low + high) / 2
        
        if check(mid):
            low = mid + 10**(-7)
        else:
            high = mid - 10**(-7)
    
    print(high)
        
        
    
 
 
 
 
T = 1
for _ in range(T):
    solve()