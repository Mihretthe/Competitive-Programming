from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    m = I()
    b = IL()
    
    """
    0 11 13 16 21 28 
    0 11 18 21 28
    """
    
    ans = 0
    
    for i in range(1, n):
        a[i] += a[i - 1]
    
    for j in range(1, m):
        b[j] += b[j - 1]
    
    
    i = 0
    j = 0
    
   
    
    while i < n and j < m:
        
        if a[i] == b[j]:
            ans += 1
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    if i == n and j == m:
        print(ans)
    else:
        print(-1)
            
        
    
    

    
 
 
 
T = 1
for _ in range(T):
    solve()