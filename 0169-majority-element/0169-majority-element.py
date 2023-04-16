class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        a=0
        while i<len(nums):
            if nums.count(nums[i])>nums.count(nums[a]):
                a=i
            i+=nums.count(nums[i])
        return nums[a]