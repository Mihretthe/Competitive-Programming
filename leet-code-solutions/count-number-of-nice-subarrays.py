class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            length = len(nums)
            left = 0
            number_subarray = 0
            counter = 0

            for right in range(length):
                if nums[right] % 2 == 1:
                    counter += 1
                print(counter)
                while left < length and counter > k:
                    if nums[left] % 2 == 1:
                        counter -= 1
                    left += 1
                number_subarray += right - left + 1
            return number_subarray

        return helper(nums, k) - helper(nums, k - 1)


