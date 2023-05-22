class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        s+="_"
        for i in range(len(t)):
            if s[i]!=t[i]:
                return t[i]