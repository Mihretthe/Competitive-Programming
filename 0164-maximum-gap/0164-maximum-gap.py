class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        max_difference = 0
        for i in range(n - 1):
            if max_difference < nums[i + 1] - nums[i]:
                max_difference = (nums[i + 1] - nums[i])
        return max_difference
        