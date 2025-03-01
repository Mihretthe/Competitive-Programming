class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        length = len(nums)
        current = 0
        maxi = 0
        for i in range(length):
            current += nums[i]
            maxi = max(maxi, current)
            if current < 0:
                current = 0
        current = 0
        mini = inf
        for i in range(length):
            current += nums[i]
            mini = min(mini, current)
            if current > 0:
                current = 0
        return max(abs(maxi), abs(mini))