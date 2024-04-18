def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil



    

def solve():
    def check(mid):
        count = 0
        for i in range(n):
            count += (ceil(d[i] / mid) * a[i])

        return count <= k

    n, k = II()
    d = IL()
    a = IL()

    left = 1
    right = max(d)
    

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    if check(left):
        print(left)
    else:
        print(-1)
    



    




    
    
    
 
T = I()
for _ in range(T):
    solve()