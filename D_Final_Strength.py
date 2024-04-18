def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil
from bisect import bisect_left
from collections import defaultdict
    

def solve():
    n = I()
    nums = IL()
    nums = [[nums[i], i] for i in range(2**n)]

    def merge(lefty, righty):
        left = [0] * len(lefty)
        right = [0] * len(righty)

        lefts = [i[0] for i in lefty]
        rights = [i[0] for i in righty]
        
        for i in range(len(lefty)):
            left[i] += bisect_left(rights, lefts[i])
            right[i] += bisect_left(lefts, rights[i])


        for i in range(len(lefty)):
            lefty[i][0] += left[i]      
            righty[i][0] += right[i]
        
        ans = []
        i = 0
        j = 0

        while i < len(lefty) and j < len(righty):
            if lefty[i][0] <= righty[j][0]:
                ans.append(lefty[i])
                i += 1
            else:
                ans.append(righty[j])
                j += 1
        ans.extend(lefty[i:])
        ans.extend(righty[j:])
        
        return ans

    def mergeSort(left, right):
        if left == right:
            return [nums[left]]
        
        mid = (left + right) // 2
        lefty = mergeSort(left, mid)
        righty = mergeSort(mid + 1, right)

        

        return merge(lefty, righty)

    answer = mergeSort(0, (2**n) - 1)
    answer.sort(key = lambda x: x[1])

    answer = list(map(lambda x : x[0], answer))

    print(*answer)
        
 
T = I()
for _ in range(T):
    solve()

    