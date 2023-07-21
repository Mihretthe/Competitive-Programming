class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(piles,k,h):
            total_hours = 0
            for pile in piles:
                hours = pile // k
                if pile % k != 0:
                    hours += 1
                total_hours += hours
                if total_hours > h:
                    return False
            return True
       
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            if isPossible(piles,m,h):
                r = m
            else:
                l = m + 1
        return l