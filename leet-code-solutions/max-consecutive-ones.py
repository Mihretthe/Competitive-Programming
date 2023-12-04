class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0 
        r = 0
        m = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                print(r,l)
                m = max(m, r - l)
                r += 1
                l = r
        m = max(m, r - l)
        return m
