class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        length = len(nums)
        previous = defaultdict(int)
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        previous[0] = -1
        prefix = 0
        result = length

        for i in range(length):
            prefix = (prefix + nums[i]) % p
            if ((prefix - remainder) % p) in previous:
                result = min(result, i - previous[(prefix - remainder) % p])
            previous[prefix] = i

        return result if result < length else -1
            