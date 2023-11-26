class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = 0
        b = len(s1) 
        s1 = sorted(s1)
        
        for r in range(len(s2)):
            s = sorted(s2[r : r + b ])
            if s == s1:
                return True            
        return False