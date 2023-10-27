class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefixes = {0:1}
        count = 0
        for i in nums:
            prefix += i
            diff = prefix - k
            if diff in prefixes:
                count += prefixes[diff]
            else:
                prefixes[diff] = 0
            if prefix in prefixes:
                prefixes[prefix] += 1
            else:
                prefixes[prefix] = 1
        return count