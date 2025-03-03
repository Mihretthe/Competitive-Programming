class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        length = len(nums)
        perimeter = 0

        for i in range(2, length):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                perimeter = max(perimeter, nums[i - 2] + nums[i - 1] + nums[i])

        return perimeter