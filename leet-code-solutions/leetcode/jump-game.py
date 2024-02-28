class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        length = len(nums)
        max_jump = 0
        
        for i in range(length):            
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
        
        return True


        
            
        