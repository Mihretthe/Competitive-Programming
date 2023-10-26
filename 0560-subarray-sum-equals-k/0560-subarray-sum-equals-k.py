class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            count += prefix_sums[complement]
            prefix_sums[prefix_sum] += 1  
        return count