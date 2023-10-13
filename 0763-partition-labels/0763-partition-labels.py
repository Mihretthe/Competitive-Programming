class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        m = len(s)
        n = m - 1
        while n >= 0:
            if s[n] in lastIdx:
                n -= 1
            else:
                lastIdx[s[n]] = n
                n -= 1
        ans = []
        i = 0
        while i < m:
            left = i
            right = lastIdx[s[i]]
            a = list(set(s[left:right]))
            
            while a:
                b = lastIdx[a.pop()]
                if b > right:                    
                    a += list(set(s[right + 1: b + 1]))
                    right = b
            ans.append(right - left + 1)
            i = right + 1                     
        return ans