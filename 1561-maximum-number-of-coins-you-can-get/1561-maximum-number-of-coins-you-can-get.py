class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        you=0
        ln=len(piles)//3
        print(ln)
        piles.sort(reverse=True)
        print(piles)
        piles=piles[:-ln]
        
        
        print(piles)
        for i in range(0,len(piles),2):
            you+=piles[i+1]
        return you