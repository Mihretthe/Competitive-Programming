class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        while n > 0:
            new = []
            
            i = 0
            c = 0
            while i + 1 < len(nums):
                if c % 2 == 0:
                    new.append(min(nums[i],nums[i + 1]))
                else:
                    new.append(max(nums[i],nums[i + 1]))
                c += 1
                i += 2
            nums = new
            n //= 2
            if n == 1:
                return nums[0]
     
                    
                