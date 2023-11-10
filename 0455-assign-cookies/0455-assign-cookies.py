class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        a = 0
        b = 0
        count = 0
        while a < len(g) and b < len(s):
            if g[a] <= s[b]:
                a += 1
                b += 1
                count += 1
            elif g[a] > s[b]:
                b += 1
        return count 
        