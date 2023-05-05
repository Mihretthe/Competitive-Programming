class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=dict(zip(s,t))
        z=""
        for i in s:
            z+=a[i]
        a=dict(zip(t,s))
        b=""
        for i in t:
            b+=a[i]        
        return z==t and b==s