class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        m = len(max(s, key = lambda x : len(x)))        
        ans = [""] * m        
        for i in range(m):            
            for j in s:
                if i < len(j):
                    ans[i] += j[i]
                else: 
                    ans[i] += " "
            ans[i] = ans[i].rstrip()
        return ans  