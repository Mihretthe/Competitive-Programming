class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        c=set()
        i=j=0
        l=0
        while i<n and j<n:
            if s[j] in c:
                c.remove(s[i])
                i+=1
            else:
                c.add(s[j])
                j+=1
                l=max(l,j-i)
        return l
                