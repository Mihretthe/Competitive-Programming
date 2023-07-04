class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)//3
        sum=0
        i=-2
        while n>0:
            sum+=piles[i]
            i-=2
            n-=1
        return sum
