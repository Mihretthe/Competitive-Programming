n, k = map(int, input().split())

nums = list(map(int, input().split()))
queries = list(map(int, input().split()))

for query in queries:
    left = -1
    right = n 

    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] >= query:
            right = mid
        else:
            left = mid

    print(right + 1)