def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter

def solve():
    n, k = II()
    nums = IL()
    counter = Counter(nums)

    my_array = []

    for key, value in counter.items():
        my_array.append(value, key)

    my_array.sort()

    left = 0
    right = k

    while left <= right:
        mid = (left + right) // 2
        count = 0

        for key, value in counter.items():
            count += value // mid

        if count == mid:
            return mid
        elif count > mid:
            right = mid - 1
        else:
            left = mid + 1

    


    
    






T = 1
for _ in range(T):
    solve()