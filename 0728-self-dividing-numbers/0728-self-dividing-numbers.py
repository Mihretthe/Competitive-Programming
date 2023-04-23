class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        n=list((range(left,right+1)))
        a=[]
        for i in n:
            s=str(i)
            c=True
            for j in s:
                if j!="0" and i%int(j)==0:
                    continue
                else:
                    c=False
                    break
            if c==True:
                a.append(i)
        return a