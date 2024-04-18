from bisect import bisect_left

length = int(input())
nums = list(map(int, input().split()))
nums.sort()
k = int(input())
answer = []

for _ in range(k):
    first, last = map(int, input().split())
    
    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= first:
            right = mid - 1
        else:
            left = mid + 1

    first = left

    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > last:
            right = mid - 1
        else:
            left = mid + 1

    answer.append(left - first)

print(*answer)