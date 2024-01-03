class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0

        l = 0
        r = 0

        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l += 1
                r += 1
                count += 1
            else:
                r += 1

        return count