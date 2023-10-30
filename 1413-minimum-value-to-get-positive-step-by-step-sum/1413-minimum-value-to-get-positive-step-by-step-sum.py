class Solution:
    def minStartValue(self, nums: List[int]) -> int:
       
        
        prefix = []
        for i in nums:
            if prefix:
                prefix.append(prefix[-1] + i)
            else:
                prefix.append(i)
        print(prefix)
        s = min(prefix)
        s = abs(0 - s)
        if min(prefix) < 1:
            return s + 1
        return 1
            