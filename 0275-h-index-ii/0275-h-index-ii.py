class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            h = n - m 
            if citations[m] >= h:
                r = m - 1
            else:
                l = m + 1
        return n - l