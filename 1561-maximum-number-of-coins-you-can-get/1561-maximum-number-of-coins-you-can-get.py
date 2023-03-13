class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me=0
        piles.sort(reverse=True)
        piles=piles[:-int(len(piles)/3)]
        for i in range(0,len(piles),2):
            me+=piles[i+1]
        return me