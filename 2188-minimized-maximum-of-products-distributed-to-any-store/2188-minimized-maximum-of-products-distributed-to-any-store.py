class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        

        def check(mid):
            count = 0

            for item in quantities:
                count += ceil(item / mid)

            return count > n

        left = 1
        right = max(quantities)

        while left <= right:
            mid = (left + right) // 2

            if not check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

