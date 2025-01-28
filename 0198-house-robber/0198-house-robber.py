class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dp(index):
            if index in memo:
                return memo[index]

            if index >= len(nums):
                return 0
            
            take = nums[index] + dp(index + 2)
            leave = dp(index + 1)

            memo[index] = max(take, leave)
            return memo[index]
        
        return dp(0)