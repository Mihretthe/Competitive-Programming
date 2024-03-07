class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)

        while left + 1 < right:
            mid = (left + right) // 2

            count = 0
            for pile in piles:
                count += ceil(pile / mid)
            
            if count > h:
                left = mid
            else:
                right = mid

        return right