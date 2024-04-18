def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

from math import ceil

global count
count = 0
def merge(left, right):
    global count
    lefty = sorted(left)
    righty = sorted(right)

    if left != lefty:

        count += 1
    
    if right != righty:
        count += 1    

    left = lefty
    right = righty

    if left[-1] + 1 != right[0] and right[-1] + 1 != left[0]:
        return 

    
    if left[0] < right[0]:
        left.extend(right)
        return left
    else:
        count += 1
        right.extend(left)
        return right

def mergeSort(nums, left, right):
    global count
    if left + 1 >= right:
        lefty = sorted(nums[left :left + 2])
        if nums[left :left + 2] != lefty:
            count += 1
        return lefty
    

    mid = (left + right) // 2
    left_side = mergeSort(nums, left, mid)
    right_side = mergeSort(nums, mid + 1, right)
    

    if not left_side or not right_side:        
        return 
    
    ans = merge(left_side, right_side)

    return ans
    
 
def solve():
    global count
    count = 0
    m = I()
    p = IL()

    if mergeSort(p, 0, m - 1):
        print(count)
    else:
        print(-1)
    

 
T = I()
for _ in range(T):
    solve()