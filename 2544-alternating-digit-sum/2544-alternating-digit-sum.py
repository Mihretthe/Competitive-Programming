class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum=0
        n=str(n)
        for i in range(len(n)):
            if i%2==0:
                sum+=int(n[i])
            else:
                sum-=int(n[i])            
        return sum