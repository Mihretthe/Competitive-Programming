class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def can(l):
            a, b, c = l
            return a + b > c

        nums.sort()
        perimeter = 0

        l = 0
        r = 3
        while r <= len(nums):
            if can(nums[l:r]):
                perimeter = max(perimeter, sum(nums[l:r]))
            l += 1
            r += 1
        return perimeter

