class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key = lambda x : x[1])
        n = max(right + 1,ranges[-1][1] + 1 )
        prefix = [0] * n
        for i, j in ranges:
            prefix[i] += 1
            if j + 1 < n:
                prefix[j + 1] -= 1
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        for i in range(left,right + 1):
            if prefix[i] <= 0:
                return False
        return True
        