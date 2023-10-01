class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = [i for i in range(1, len(nums) + 1)]
        nums = set([i for i in nums if i > 0])
        # m = min(nums)
        ans = []
        
        for i in n:
            if i not in nums:
                return i
        return len(nums) + 1
        
        
            