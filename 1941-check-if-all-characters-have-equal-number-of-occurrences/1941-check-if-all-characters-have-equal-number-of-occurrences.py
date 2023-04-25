class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=set()
        b=[]
        for i in s:
            b.append(i)
        for i in s:     
            a.add(i)
        n=list(a)
        z=b.count(n[0])
        
        for i in n:
            if b.count(i)!=z:
                return False
        return True