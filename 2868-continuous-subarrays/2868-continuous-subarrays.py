class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0 
        length = len(nums)
        number = 0
        counter = defaultdict(int)

        for right in range(length):
            counter[nums[right]] += 1

            while max(counter) - min(counter) > 2:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            number += right - left + 1
        
        return number