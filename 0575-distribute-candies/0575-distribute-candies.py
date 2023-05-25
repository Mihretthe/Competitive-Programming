class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(candyType)//2
        return min(a,len(set(candyType)))
        
        