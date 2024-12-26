class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        memo = {}
        count = 0

        def dp(index, current):
            nonlocal count
            if (index, current) in memo:
                return memo[(index, current)]
            
            if index == length:
                if current == target:
                    return 1
                return 0
            for i in [True, False]:
                if i:
                    memo[(index, current)] = dp(index + 1, current + nums[index])
                else:
                    memo[(index, current)] += dp(index + 1, current - nums[index])
            return memo[(index, current)]

        return dp(0, 0)
        
            


