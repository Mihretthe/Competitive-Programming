def canBeSorted(nums, n):
    i = 1
    while i < n - 1:
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i = 1
        else:
            i += 1
    r = list(range(1, n + 1))
    return r == nums

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if canBeSorted(nums,n):
        print("YES")
    else:
        print("NO")
