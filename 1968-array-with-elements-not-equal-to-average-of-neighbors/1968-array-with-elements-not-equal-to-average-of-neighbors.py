class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)-1):    
                s= nums[i-1]+nums[i+1]
                if int(s/2) == nums[i]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        for i in range(1,len(nums)-1):    
                s= nums[i-1]+nums[i+1]
                if int(s/2) == nums[i]:
                    self.rearrangeArray(nums)
        return nums
             