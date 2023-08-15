class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, (n+1)//2, int(1e9 + 7)) * pow(4, n//2, int(1e9 + 7))) % int(1e9 + 7)
            
            