class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        r = k - 1
        n = len(nums)
        m = -1 * float('inf')
        s = sum(nums[l:k])
        while r < n:        
            ave = s / k
            m = max(ave, m)
            s -= nums[l]
            if r + 1 < n:
                s += nums[r + 1]
            l += 1
            r += 1
           
        return m