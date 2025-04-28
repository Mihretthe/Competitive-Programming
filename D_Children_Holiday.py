from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

"""
- inflate m ballons
- n assistances
- ith assistant inflate a ballon in ti minute, after he/she inflate zi ballon he/she rest for yi minute 
- print the optimal time and for each assistant how many ballon they inflate


2, 1, 1

3
1 

"""

def solve():
    m, n = II()
    
    array = []
    
    for _ in range(n):
        t, z, y = II()
        array.append((t, z, y))
    
    def check(mid):
        pass
            
        

    low = 0
    high = 5
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1
            
            
    print(low, high)
 
 
 
 
T = 1
for _ in range(T):
    solve()