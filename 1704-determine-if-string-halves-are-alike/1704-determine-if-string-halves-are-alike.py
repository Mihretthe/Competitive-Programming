class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c=0
        n="aeiouAEIOU"
        l=0
        r=len(s)-1
        while l<r:
            if s[l] in n:
                c+=1
            if s[r] in n:
                c-=1
            l+=1
            r-=1
        return c==0