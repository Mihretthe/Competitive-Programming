class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #Sliding Window
        def helper(k):
            length = len(nums)
            left = 0
            sum = 0
            no_subarrays = 0

            for right in range(length):
                sum += nums[right]
                while left < length and sum > k:
                    sum -= nums[left]
                    left += 1
                no_subarrays += (right - left + 1)
            
            return no_subarrays

        if goal == 0:
            return helper(goal)

        return helper(goal) - helper(goal - 1)

