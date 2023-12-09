def canBeReversed(nums, k, n):
    if n > 1:
        l = 0
        r = 1
        while r < n:
            while r < n and nums[l] <= nums[r]:
                l += 1
                r += 1

                
            
            if r - l <= k:
                nums[l:r + 1] = nums[l:r + 1][::-1]
            else:
                return False

        return sorted(nums) == nums
    else:
        return True
    
for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    if canBeReversed(nums, k, n):
        print("YES")
    else:
        print("NO")