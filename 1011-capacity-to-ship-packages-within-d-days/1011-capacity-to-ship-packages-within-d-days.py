class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isPossible(weights, capacity, days):
            curr = 0
            d = 1
            for i in weights:
                curr += i
                if curr > capacity:
                    d += 1
                    curr = i
            return d <= days
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2
            if isPossible(weights, m, days):
                r = m
            else:
                l = m + 1
        return l