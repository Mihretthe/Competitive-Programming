class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div(nums, m):
            s = 0
            for i in nums:
                s += (ceil(i/m))
            return s
        l = 1
        r = max(nums)
        while l < r:
            m = (l + r) // 2
            if div(nums, m) <= threshold:
                r = m
            else:
                l = m + 1
        return l