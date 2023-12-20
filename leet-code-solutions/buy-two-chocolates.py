class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        leftover = money - (prices[0] + prices[1])

        if leftover < 0:
            return money
        return leftover