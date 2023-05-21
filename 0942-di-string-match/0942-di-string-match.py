class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=0
        r=len(s)
        a=list((range(len(s)+1)))
        b=[]
        for i in range(len(s)):
            if s[i]=="I":
                b.append(a[l])
                l+=1
            elif s[i]=="D":
                b.append(a[r])
                r-=1
        b+=[i for i in a if i not in b]
        return b