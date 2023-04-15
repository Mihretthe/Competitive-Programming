class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=True
        if len(s)!=len(t):
            return False
        for i in s:
            if i in t:
                if s.count(i)!=t.count(i):
                    return False
            else:
                c=False
        for i in t:
            if i in s:
                continue
            else:
                c=False
        return c