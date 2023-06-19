class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        a=[0 for i in range(highLimit)]
        for i in range(lowLimit,highLimit+1):
            i=str(i)
            i=sum(int(j) for j in i)
            a[i-1]+=1
        return max(a)
                     
            