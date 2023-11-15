class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l = 0
        r = 0
        n = len(chars)
        
        while r < n:
            while r < n and chars[r] == chars[l] :
                r += 1
            if r - l > 1:
                s += chars[l] + str(r - l)
            else:
                s += chars[l]
            
            l = r      
        print(s)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)