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
    ans = [0] * n

    i = 0
    index = 0

    while i < n:
        ans[i] = a[index]
        index += 1
        i += 2
    index = -1
    i = 1
    while i < n:
        ans[i] = a[index]
        index -= 1
        i += 2
    
    print(*ans)



    
    
 
 
T = 1
for _ in range(T):
    solve()