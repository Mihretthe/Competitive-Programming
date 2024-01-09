class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        l, r = 0, 0
        n = len(nums)
        
        if 0 not in nums:
            return n - 1
        
        count = 0
        idx = 0
        ans = 0
        zero = 0
        while r < n:
            if nums[l] == nums[r] == 0:
                l += 1
                r += 1
            elif nums[r] == 1:
                count += 1
                r += 1
            elif nums[r] == 0 and zero == 1:
                l = idx + 1
                r = idx + 1
                ans = max(ans,count)
                count = 0
                zero = 0
            else:                
                idx = r
                r += 1
                zero += 1
        ans = max(ans, count)
        
                
        return ans