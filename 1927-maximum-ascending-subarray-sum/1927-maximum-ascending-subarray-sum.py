class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = nums[0]
        so_far = nums[0]

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                so_far += nums[i]
            else:
                maxi = max(maxi, so_far)
                so_far = nums[i]
        
        maxi = max(maxi, so_far)

        return maxi

            