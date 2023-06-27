class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=0
        j=k-1
        c=list(range(1,n+1))
        while len(c)>1:            
            while j>=len(c):
                j-=len(c)
            c.remove(c[j])
            i=j
            j=i+k-1
            
        return c[0]
        