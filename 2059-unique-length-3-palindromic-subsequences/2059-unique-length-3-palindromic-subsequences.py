class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        hashset = set()
        ans = 0
        
        for i in range(n):
            if s[i] in hashset:
                continue
            r = n - 1
            while (r - i) >= 2:
                if s[i] == s[r]:
                    a = set(s[i + 1: r])
                    ans += len(a)
                    hashset.add(s[i])
                    break
                else:
                    r -= 1
        return ans
                    
                        
