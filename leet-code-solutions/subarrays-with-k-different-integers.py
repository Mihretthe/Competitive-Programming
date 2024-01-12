class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            left = 0
            length = len(nums)
            sum_k = 0
            counter = defaultdict(int)

            for right in range(length):
                counter[nums[right]] += 1
                while left < length and len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                sum_k += right - left + 1
            
            return sum_k

        return helper(nums, k) - helper(nums, k - 1)