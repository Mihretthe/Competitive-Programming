class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        
        prefix = [0] * n
        for i, j in requests:
            prefix[i] += 1
            if j + 1 < n:
                prefix[j + 1] -= 1
        def doPrefix(l):
            for i in range(1,len(l)):
                l[i] += l[i - 1]
            
            return l
        
        prefix = doPrefix(prefix)
        prefix.sort(reverse = True) 
        nums.sort(reverse = True)
        ans = 0
        
        for i in range(n):
            if prefix[i] == 0:
                break
            ans += (nums[i] * prefix[i])

        
        
        
        
        return ans % int(1e9 + 7)