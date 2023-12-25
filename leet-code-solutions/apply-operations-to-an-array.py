class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0
        nums.sort(key = lambda x : x == 0)
        
        return nums
