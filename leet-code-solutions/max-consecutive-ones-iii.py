class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_z = 0
        n = len(nums)
        max_length = 0

        for right in range(n):
            if nums[right] == 0:
                count_z += 1

            if nums[right] == 0 and count_z > k:
                count_z -= 1
                max_length = max(max_length, right - left)
                while left < right and nums[left] != 0:
                    left += 1
                left += 1
        max_length = max(max_length, n - left)
        return max_length

                

        
             