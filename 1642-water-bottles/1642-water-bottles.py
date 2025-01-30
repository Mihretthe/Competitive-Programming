class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles>=numExchange:
            rem=numBottles%numExchange
            diff=numBottles//numExchange
            ans+=diff
            numBottles=rem+diff

        return ans

        