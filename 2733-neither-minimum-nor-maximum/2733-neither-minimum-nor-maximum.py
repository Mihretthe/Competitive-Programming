class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)<=2:
            return -1
        return nums[1]