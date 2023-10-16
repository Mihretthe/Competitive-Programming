class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while n > 0:
            
            new = []
            for i in range(1,n):
                new.append((nums[i - 1] + nums[i])%10)
            nums = new
            n -= 1
            if n == 1:
                return new[0]
        
        
            