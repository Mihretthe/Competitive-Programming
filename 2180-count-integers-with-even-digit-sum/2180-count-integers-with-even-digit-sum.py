class Solution:
    def countEven(self, num: int) -> int:
        l=list((range(1,num+1)))
        a=[]
        for i in l:
            s=str(i)
            if len(s)==1 and i%2==0:
                a.append(i)
            else:
                b=0
                for j in s:
                    b+=int(j)
                if b%2==0:
                    a.append(i)
                else:
                    continue
        return len(a)