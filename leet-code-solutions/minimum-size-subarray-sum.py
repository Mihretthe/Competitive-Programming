class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subarray_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            subarray_sum += nums[right]
            if subarray_sum >= target:
                while target <= subarray_sum - nums[left]:
                    subarray_sum -= nums[left]
                    left += 1
                min_length = min(min_length, right - left + 1)
        if subarray_sum >= target:
            min_length = min(min_length, right - left + 1)
        else:
            return 0
        return min_length

            
            
