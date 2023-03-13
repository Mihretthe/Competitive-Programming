class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        you=0
        ln=len(piles)//3
        piles.sort(reverse=True)
        piles=piles[:-ln]
        for i in range(0,len(piles),2):
            you+=piles[i+1]
        return you