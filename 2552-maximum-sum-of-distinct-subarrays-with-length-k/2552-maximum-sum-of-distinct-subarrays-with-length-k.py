class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = 0
        counter = Counter()
        total = 0
        maxi = 0

        for right in range(length):
            counter[nums[right]] += 1 

            while left <= right and counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                total -= nums[left]
                left += 1

            total += nums[right]
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                total -= nums[left]
                left += 1
            if len(counter) == k:
                maxi = max(maxi, total)
        
        return maxi