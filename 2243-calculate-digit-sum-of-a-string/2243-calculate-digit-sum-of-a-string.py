class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        m = len(s)
        while m != k:
            if m < k:
                break
            new = ""
            i = k
            while i < len(s) + k:
                a = s[i - k:i]
                n = 0
                for j in a:
                    n += int(j)
                new += str(n) 
                i += k
            s = new
            m = len(s)
            
        return s
                
            