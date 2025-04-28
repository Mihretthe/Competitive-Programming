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
    
    a.sort()
    
    
    answer = [a[0]]
    
    left = 1
    right = 2*n - 1
    
    num = 0
    
    while left < right:
        answer.append(a[left])
        answer.append(a[right])
        num += (a[left] - a[right])
        
        left += 1
        right -= 1
    
    """
    small_num = num + x - a[left]
    x = small_num - num + a[left]
    """
    x = a[0] - num + a[left]
    answer.append(x)
    answer.append(a[left])
    
    
    print(*answer)
    
    
    
    
    
    
    
 
 
 
T = I()
for _ in range(T):
    solve()