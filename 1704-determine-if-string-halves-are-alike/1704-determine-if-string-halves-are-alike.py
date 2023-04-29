class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        c=0
        d=0
        n="aeiouAEIOU"
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        for i in a:
            if i in n:
                c+=1
        for i in b:
            if i in n:
                d+=1
        return c==d