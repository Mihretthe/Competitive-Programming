
def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from collections import Counter

from bisect import bisect_right, bisect_left




def solve():
    length = I()
    nums = IL()
    min_value = float('inf')

    def check(mid):

        for i in range(length):
            if i == 0:
                a = (nums[i] - 2 * mid) + (nums[i + 1] - mid)
                if a <= 0:
                    return True
            elif i == length - 1:
                b = (nums[i - 1] - 2 * mid) + (nums[i] - mid)
                if b <= 0:
                    return True
            else:
                a = (nums[i] - 2 * mid) + (nums[i + 1] - mid)
                b = (nums[i - 1] - 2 * mid) + (nums[i] - mid)       
                c = (nums[i - 1] - mid) + (nums[i + 1] - mid)  

                if a <= 0 or b <= 0 or c <= 0:
                    return True
    

    low = 0
    high = max(nums) 

    while low + 1 < high:
        mid = (low + high) // 2

        if check(mid):
            high = mid 
        else:
            low = mid 
    
    print(min(high, sum(sorted(nums)[:2])))
    

T = 1
for _ in range(T):
    solve()