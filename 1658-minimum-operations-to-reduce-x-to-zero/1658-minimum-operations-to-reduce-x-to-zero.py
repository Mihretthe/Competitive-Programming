class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:        
        t = sum(nums) - x

        if t == 0:
            return len(nums)

        n = len(nums)
        l = 0
        c = 0
        m = float('inf')

        for r in range(n):
            c += nums[r]

            while c > t and l <= r:
                c -= nums[l]
                l += 1

            if c == t:
                m = min(m, n - (r - l + 1))

        if m == float('inf'):
            return -1
        else:
            return m 
