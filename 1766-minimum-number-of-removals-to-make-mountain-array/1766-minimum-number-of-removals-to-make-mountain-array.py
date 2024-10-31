class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        length = len(nums)

        dp = [0] * length


        for i in range(length - 1, -1, -1):
            maxi = 0
            for j in range(i + 1, length):
                if nums[j] < nums[i]:
                    maxi = max(maxi, dp[j] + 1)
        
            dp[i] = maxi


        new = [0] * length
        for i in range(length):
            maxi = 0
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    maxi = max(maxi, new[j] + 1)
            
           
            new[i] = maxi

        maxi = 0
        for i in range(length):
            if dp[i] != 0 and new[i] != 0:
                maxi = max(maxi, dp[i] + new[i] + 1)
        
       

        return length - maxi
