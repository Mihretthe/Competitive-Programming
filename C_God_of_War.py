from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heappop, heappush

def solve():
    n = I()
    array = []
    for _ in range(n):
        a = IL()
        k = a[0]
        a = a[1:]
        
        maxi = max(a)
        index = a.index(maxi)
        needed = max(a[0] + 1, maxi - index + 1)
        heappush(array, (needed, -k))

    
    need, many = heappop(array)
    answer = need - many
    ans = need
    while array:
        need, many = heappop(array)
        many = -many
        if answer < need:
            left = need - answer
            answer = need
            ans += left
        answer += many

    print(ans)

        
        
    

    
    
 
 
 
 
T = I()
for _ in range(T):
    solve()