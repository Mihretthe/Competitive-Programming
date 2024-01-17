class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        previous_sum = defaultdict(int)
        subarrays = 0
        prefix = 0
        previous_sum[0] = 1
        
        for num in nums:
            prefix += num
            if prefix - k in previous_sum:
                subarrays += previous_sum[prefix - k]
            previous_sum[prefix] += 1
        return subarrays