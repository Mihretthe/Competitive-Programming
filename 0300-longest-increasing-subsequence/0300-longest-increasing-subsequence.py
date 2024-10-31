class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length

        for i in range(length - 1, -1, -1):
            maxi = 0
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    maxi = max(maxi, dp[j] + 1)
            dp[i] = maxi

        return max(dp) + 1

        
                