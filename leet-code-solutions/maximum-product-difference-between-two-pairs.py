class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a, b, c, d = nums[0], nums[1], nums[-1], nums[-2]
        return (c * d) - (a * b)