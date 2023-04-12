class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if nums.count(nums[i])==3:
                i+=3
            else:
                return nums[i]