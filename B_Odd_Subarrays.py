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
    
    count = 0
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            count += 1
            i += 1
        i += 1
        
    
    print(count)
 
 
 
 
T = I()
for _ in range(T):
    solve()