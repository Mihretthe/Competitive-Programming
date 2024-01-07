class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        max_average = s / k
        l = 1
        r = k 


        while r < len(nums):
            s -= nums[l - 1]
            s += nums[r]
            max_average = max(max_average, s / k)
            l += 1
            r += 1
        
        return max_average
            