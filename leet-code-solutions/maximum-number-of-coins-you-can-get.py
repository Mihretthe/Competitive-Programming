class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles) 
        i = 1
        max_coins = 0

        while n:
            max_coins += piles[i]
            i += 2
            n -= 3

        return max_coins
