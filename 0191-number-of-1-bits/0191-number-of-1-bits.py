class Solution:
    def hammingWeight(self, n: int) -> int:
        a=[]
        while n>0:
            a.append(n%2)
            n=n//2
        return a.count(1)