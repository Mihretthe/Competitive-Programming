class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        
        if k % 2:
            return self.kthGrammar(n, ceil(k / 2))
        
        if self.kthGrammar(n, ceil(k / 2)):
            return 0
        else:
            return 1        