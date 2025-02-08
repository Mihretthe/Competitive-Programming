from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    a = IL()
    
    index = 1
    count = 1
    maxi = 1
    
    
    while index < n:
        if a[index] == a[index - 1]:
            maxi = max(maxi, count)
            count = 1
        else:
            count += 1
        
        index += 1
    maxi = max(maxi, count)
    print(maxi)
        
 
 
 
T = 1
for _ in range(T):
    solve()