class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        prefix = [0] * 1000001
        print(len(intervals))

        for left, right in intervals:
            prefix[left] += 1
            if right + 1 < 1000001:
                prefix[right + 1] -= 1
        
        for i in range(1, 1000001):
            prefix[i] += prefix[i - 1]
        
        
        return max(prefix)