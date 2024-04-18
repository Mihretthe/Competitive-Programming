
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter
 
def solve():
    n = I()
    a = IL()
    m = I()
    q = IL()

    prefix = []

    for i in a:
        if prefix:
            prefix.append(prefix[-1] + i)
        else:
            prefix.append(i)
    
    for i in q:
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if prefix[mid] == i:
                print(mid + 1) 
                break
            elif prefix[mid] > i:
                right = mid - 1
            else:
                left = mid + 1

        else:
            print(left + 1)


    
 
 
T = 1
for _ in range(T):
    solve()