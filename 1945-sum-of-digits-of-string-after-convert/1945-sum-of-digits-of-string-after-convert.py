class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l=string.ascii_lowercase    
        b=""
        for i in s:
            b+=str(l.index(i)+1)
        while k>0:
            n=0
            for i in b:
                n+=int(i)
            b=str(n)
            k-=1
        return n