class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=[]
        for i in set(s):
            if s.count(i)==1:
                a.append(s.index(i))
        return min(a) if len(a)>0 else -1
        