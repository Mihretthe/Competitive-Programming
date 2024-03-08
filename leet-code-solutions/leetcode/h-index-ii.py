class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = max(citations) + 1
        length = len(citations)

        while left + 1 < right:
            mid = (left + right) // 2
            index = bisect_left(citations, mid)

            if mid > length - index:
                right = mid
            else:
                left = mid

        return left