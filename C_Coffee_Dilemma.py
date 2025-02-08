from sys import stdin

def I(): return int(stdin.readline().strdef merge(left_half, right_half):
    left_index = 0
    right_index = 0
    sorted_subarray = []
   
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_subarray.append(left_half[left_index])
            left_index += 1
        else:
            sorted_subarray.append(right_half[right_index])
            right_index += 1
           
    sorted_subarray.extend(left_half[left_index:])
    sorted_subarray.extend(right_half[right_index:])
   
    return sorted_subarray
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)ip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heappop, heappush

def solve():
    n = I()
    a = IL()

    total = 0 
    heap = []

    for i in a:
        total += i 
        heappush(heap, i)

        while total < 0:
            total -= heappop(heap)
    
    print(len(heap))
 
 
 
 
T = 1
for _ in range(T):
    solve()